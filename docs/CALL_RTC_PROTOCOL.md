# ممیزی تماس و سیگنالینگ RTC بله — ۲۰۲۶-۰۹-۰۱

## نتیجه

تماس صوتی/تصویری بله دو لایهٔ مستقل دارد:

1. سرویس `bale.meet.v1.Meet` روی gRPC-Web برای ساخت، ورود، مدیریت اعضا، ضبط و
   پایان تماس؛
2. LiveKit روی WebSocket و WebRTC برای سیگنالینگ و انتقال رسانه.

URL بررسی‌شده متعلق به لایهٔ دوم است. مسیر آن از الگوی
`wss://<meet-shard>/<instance>/rtc/v1` استفاده می‌کند و دو پارامتر محرمانه دارد:

- `access_token`: یک JWT کوتاه‌عمر با grantهای استاندارد LiveKit؛
- `join_request`: پیام protobuf از نوع `livekit.WrappedJoinRequest` با
  base64url، که در این نمونه payload آن با gzip فشرده شده است.

JWT فقط decode می‌شود و اعتبار امضای آن بدون کلید صادرکننده قابل اثبات نیست.
نمونهٔ بررسی‌شده یک بازهٔ اعتبار شش‌ساعته و مجوزهای publish، subscribe، join و
room-admin داشت، اما publish-data در آن خاموش بود. شناسه‌ها و token در فایل‌های
ممیزی ذخیره نشده‌اند.

## RPCهای مدیریت تماس بله

build رسمی `web@5.5.1+169491` دقیقاً ۳۰ RPC زیر را منتشر می‌کند. هر ۳۰ مورد با
registry و schema فعلی BaleNova برابرند؛ در diff این سرویس هیچ متد اضافه، حذف یا
تغییر‌یافته‌ای وجود ندارد.

| گروه | RPCها |
|---|---|
| تماس خصوصی | `StartCall`, `AcceptCall`, `ReceiveCall`, `DiscardCall` |
| تماس گروهی | `StartGroupCall`, `JoinGroupCall`, `LeaveGroupCall`, `GetGroupCall`, `GetCallState` |
| دسترسی اتصال | `GetWssURL` |
| اعضا و درخواست ورود | `InviteToCall`, `AskToJoinCall`, `AnswerCallJoinRequest`, `MuteParticipant`, `RemoveParticipant`, `TakeCallAction` |
| لینک | `GenerateCallLink`, `GetCallLinkDetails`, `SetLinkTitle` |
| گزارش و وضعیت | `GetCallLogs`, `GetOngoingCalls`, `DeleteCallLogs`, `SubmitCallFeedback` |
| ضبط/پخش | `StartRecording`, `StopRecording`, `UpdateLayout`, `StartStream`, `DeleteStream` |
| رویداد | `SendCallReaction`, `SendFanoosEvent` |

فیلد، شمارهٔ wire و codec ورودی/خروجی همهٔ این RPCها در
`protocol/official-web-5.5.1.json` ثبت شده است.

## handshake اتصال `/rtc/v1`

SDK مرورگر این ترتیب را اجرا می‌کند:

1. از URL پایه و JWT یک URL سیگنالینگ می‌سازد؛
2. `livekit.JoinRequest` را serialize می‌کند؛
3. در صورت پشتیبانی مرورگر آن را با gzip فشرده می‌کند؛
4. نتیجه را در `livekit.WrappedJoinRequest` می‌گذارد؛
5. wrapper را base64url کرده و با نام `join_request` کنار `access_token` به URL
   اضافه می‌کند؛
6. اولین frame سرور باید `livekit.SignalResponse` از نوع `join` یا در اتصال
   مجدد از نوع `reconnect` باشد؛
7. frameهای باینری بعدی protobufهای `SignalRequest` و `SignalResponse` هستند.

`WrappedJoinRequest` دو فیلد دارد:

| شماره | نام | نوع |
|---:|---|---|
| 1 | `compression` | enum: `NONE=0`, `GZIP=1` |
| 2 | `join_request` | bytes: serialized/compressed `JoinRequest` |

`JoinRequest` نیز این فیلدها را دارد:

| شماره | نام | نوع |
|---:|---|---|
| 1 | `client_info` | `ClientInfo` |
| 2 | `connection_settings` | `ConnectionSettings` |
| 3 | `metadata` | string |
| 4 | `participant_attributes` | map<string,string> |
| 5 | `add_track_requests` | repeated `AddTrackRequest` |
| 6 | `publisher_offer` | `SessionDescription` |
| 7 | `reconnect` | bool |
| 8 | `reconnect_reason` | enum |
| 9 | `participant_sid` | string |
| 10 | `sync_state` | `SyncState` |

## پیام‌های سیگنالینگ

ورودی‌های client→server در `livekit.SignalRequest`:

| شماره | variant |
|---:|---|
| 1 | `offer` |
| 2 | `answer` |
| 3 | `trickle` |
| 4 | `add_track` |
| 5 | `mute` |
| 6 | `subscription` |
| 7 | `track_setting` |
| 8 | `leave` |
| 10 | `update_layers` (deprecated) |
| 11 | `subscription_permission` |
| 12 | `sync_state` |
| 13 | `simulate` |
| 14 | `ping` (deprecated) |
| 15 | `update_metadata` |
| 16 | `ping_req` |
| 17 | `update_audio_track` |
| 18 | `update_video_track` |
| 19 | `publish_data_track_request` |
| 20 | `unpublish_data_track_request` |
| 21 | `update_data_subscription` |
| 22 | `store_data_blob_request` |
| 23 | `get_data_blob_request` |

خروجی‌های server→client در `livekit.SignalResponse`:

| شماره | variant |
|---:|---|
| 1 | `join` |
| 2 | `answer` |
| 3 | `offer` |
| 4 | `trickle` |
| 5 | `update` |
| 6 | `track_published` |
| 8 | `leave` |
| 9 | `mute` |
| 10 | `speakers_changed` |
| 11 | `room_update` |
| 12 | `connection_quality` |
| 13 | `stream_state_update` |
| 14 | `subscribed_quality_update` |
| 15 | `subscription_permission_update` |
| 16 | `refresh_token` |
| 17 | `track_unpublished` |
| 18 | `pong` (deprecated) |
| 19 | `reconnect` |
| 20 | `pong_resp` |
| 21 | `subscription_response` |
| 22 | `request_response` |
| 23 | `track_subscribed` |
| 24 | `room_moved` |
| 25 | `media_sections_requirement` |
| 26 | `subscribed_audio_codec_update` |

پیاده‌سازی مستقیم offer/answer/ICE در BaleNova انجام نشده است. این پیام‌ها به
نسخهٔ WebRTC و state داخلی SDK وابسته‌اند و `livekit.rtc.Room` آن‌ها را همراه با
reconnect، TURN، subscription و media negotiation مدیریت می‌کند.

## API اضافه‌شده به BaleNova

```python
connection = await client.join_group_call_rtc(call_id, "My client")
print(connection.permissions.can_publish)

room = await connection.connect()  # نیازمند balenova[voice]
# publish/subscribe با API رسمی livekit.rtc

await room.disconnect()
await client.leave_group_call(call_id)
```

برای تحلیل URL ثبت‌شده بدون چاپ secret:

```python
from balenova import parse_call_wss_url

connection = parse_call_wss_url(captured_url)
print(connection)  # token، room، subject و protobuf را نمایش نمی‌دهد
print(connection.join_request.compression if connection.join_request else None)
```

توابع عمومی جدید عبارت‌اند از `parse_call_wss_url`،
`decode_livekit_join_request`، `call_rtc_connection_from_group_call` و متد
`Client.join_group_call_rtc`. Decoder برای payload فشرده سقف یک مگابایت دارد.

## منابع تطبیق

- [LiveKit protocol: livekit_rtc.proto](https://github.com/livekit/protocol/blob/f49f4aa3955b90b3c0f2a9a8afcde3023a66688a/protobufs/livekit_rtc.proto)
- [LiveKit JS SignalClient](https://github.com/livekit/client-sdk-js/blob/c2eb1324354da78069f4c31e371a9b6101b3417f/src/api/SignalClient.ts)
- catalog محلی build رسمی بله: `protocol/official-web-5.5.1.json`

سورس LiveKit برای شکل wrapper و frameها مرجع اصلی است؛ grantها و endpoint بله از
capture مجاز حساب و build رسمی بله به دست آمده‌اند.
