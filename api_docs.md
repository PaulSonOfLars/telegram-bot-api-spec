# 📖 Telegram Bot API Documentation
**Version**: `Bot API 7.10`
**Release Date**: `September 6, 2024`
[🔗 Changelog](https://core.telegram.org/bots/api#september-6-2024)

---
## ✨ Introduction
This document contains the detailed specifications of the Telegram Bot API, including methods and types.
You can quickly navigate to the specific methods or types by clicking on the links below:
### 🚀 Methods
- [getUpdates](#getupdates)
- [setWebhook](#setwebhook)
- [deleteWebhook](#deletewebhook)
- [getWebhookInfo](#getwebhookinfo)
- [getMe](#getme)
- [logOut](#logout)
- [close](#close)
- [sendMessage](#sendmessage)
- [forwardMessage](#forwardmessage)
- [forwardMessages](#forwardmessages)
- [copyMessage](#copymessage)
- [copyMessages](#copymessages)
- [sendPhoto](#sendphoto)
- [sendAudio](#sendaudio)
- [sendDocument](#senddocument)
- [sendVideo](#sendvideo)
- [sendAnimation](#sendanimation)
- [sendVoice](#sendvoice)
- [sendVideoNote](#sendvideonote)
- [sendPaidMedia](#sendpaidmedia)
- [sendMediaGroup](#sendmediagroup)
- [sendLocation](#sendlocation)
- [sendVenue](#sendvenue)
- [sendContact](#sendcontact)
- [sendPoll](#sendpoll)
- [sendDice](#senddice)
- [sendChatAction](#sendchataction)
- [setMessageReaction](#setmessagereaction)
- [getUserProfilePhotos](#getuserprofilephotos)
- [getFile](#getfile)
- [banChatMember](#banchatmember)
- [unbanChatMember](#unbanchatmember)
- [restrictChatMember](#restrictchatmember)
- [promoteChatMember](#promotechatmember)
- [setChatAdministratorCustomTitle](#setchatadministratorcustomtitle)
- [banChatSenderChat](#banchatsenderchat)
- [unbanChatSenderChat](#unbanchatsenderchat)
- [setChatPermissions](#setchatpermissions)
- [exportChatInviteLink](#exportchatinvitelink)
- [createChatInviteLink](#createchatinvitelink)
- [editChatInviteLink](#editchatinvitelink)
- [createChatSubscriptionInviteLink](#createchatsubscriptioninvitelink)
- [editChatSubscriptionInviteLink](#editchatsubscriptioninvitelink)
- [revokeChatInviteLink](#revokechatinvitelink)
- [approveChatJoinRequest](#approvechatjoinrequest)
- [declineChatJoinRequest](#declinechatjoinrequest)
- [setChatPhoto](#setchatphoto)
- [deleteChatPhoto](#deletechatphoto)
- [setChatTitle](#setchattitle)
- [setChatDescription](#setchatdescription)
- [pinChatMessage](#pinchatmessage)
- [unpinChatMessage](#unpinchatmessage)
- [unpinAllChatMessages](#unpinallchatmessages)
- [leaveChat](#leavechat)
- [getChat](#getchat)
- [getChatAdministrators](#getchatadministrators)
- [getChatMemberCount](#getchatmembercount)
- [getChatMember](#getchatmember)
- [setChatStickerSet](#setchatstickerset)
- [deleteChatStickerSet](#deletechatstickerset)
- [getForumTopicIconStickers](#getforumtopiciconstickers)
- [createForumTopic](#createforumtopic)
- [editForumTopic](#editforumtopic)
- [closeForumTopic](#closeforumtopic)
- [reopenForumTopic](#reopenforumtopic)
- [deleteForumTopic](#deleteforumtopic)
- [unpinAllForumTopicMessages](#unpinallforumtopicmessages)
- [editGeneralForumTopic](#editgeneralforumtopic)
- [closeGeneralForumTopic](#closegeneralforumtopic)
- [reopenGeneralForumTopic](#reopengeneralforumtopic)
- [hideGeneralForumTopic](#hidegeneralforumtopic)
- [unhideGeneralForumTopic](#unhidegeneralforumtopic)
- [unpinAllGeneralForumTopicMessages](#unpinallgeneralforumtopicmessages)
- [answerCallbackQuery](#answercallbackquery)
- [getUserChatBoosts](#getuserchatboosts)
- [getBusinessConnection](#getbusinessconnection)
- [setMyCommands](#setmycommands)
- [deleteMyCommands](#deletemycommands)
- [getMyCommands](#getmycommands)
- [setMyName](#setmyname)
- [getMyName](#getmyname)
- [setMyDescription](#setmydescription)
- [getMyDescription](#getmydescription)
- [setMyShortDescription](#setmyshortdescription)
- [getMyShortDescription](#getmyshortdescription)
- [setChatMenuButton](#setchatmenubutton)
- [getChatMenuButton](#getchatmenubutton)
- [setMyDefaultAdministratorRights](#setmydefaultadministratorrights)
- [getMyDefaultAdministratorRights](#getmydefaultadministratorrights)
- [editMessageText](#editmessagetext)
- [editMessageCaption](#editmessagecaption)
- [editMessageMedia](#editmessagemedia)
- [editMessageLiveLocation](#editmessagelivelocation)
- [stopMessageLiveLocation](#stopmessagelivelocation)
- [editMessageReplyMarkup](#editmessagereplymarkup)
- [stopPoll](#stoppoll)
- [deleteMessage](#deletemessage)
- [deleteMessages](#deletemessages)
- [sendSticker](#sendsticker)
- [getStickerSet](#getstickerset)
- [getCustomEmojiStickers](#getcustomemojistickers)
- [uploadStickerFile](#uploadstickerfile)
- [createNewStickerSet](#createnewstickerset)
- [addStickerToSet](#addstickertoset)
- [setStickerPositionInSet](#setstickerpositioninset)
- [deleteStickerFromSet](#deletestickerfromset)
- [replaceStickerInSet](#replacestickerinset)
- [setStickerEmojiList](#setstickeremojilist)
- [setStickerKeywords](#setstickerkeywords)
- [setStickerMaskPosition](#setstickermaskposition)
- [setStickerSetTitle](#setstickersettitle)
- [setStickerSetThumbnail](#setstickersetthumbnail)
- [setCustomEmojiStickerSetThumbnail](#setcustomemojistickersetthumbnail)
- [deleteStickerSet](#deletestickerset)
- [answerInlineQuery](#answerinlinequery)
- [answerWebAppQuery](#answerwebappquery)
- [sendInvoice](#sendinvoice)
- [createInvoiceLink](#createinvoicelink)
- [answerShippingQuery](#answershippingquery)
- [answerPreCheckoutQuery](#answerprecheckoutquery)
- [getStarTransactions](#getstartransactions)
- [refundStarPayment](#refundstarpayment)
- [setPassportDataErrors](#setpassportdataerrors)
- [sendGame](#sendgame)
- [setGameScore](#setgamescore)
- [getGameHighScores](#getgamehighscores)
### 🛠️ Types
- [Update](#update)
- [WebhookInfo](#webhookinfo)
- [User](#user)
- [Chat](#chat)
- [ChatFullInfo](#chatfullinfo)
- [Message](#message)
- [MessageId](#messageid)
- [InaccessibleMessage](#inaccessiblemessage)
- [MaybeInaccessibleMessage](#maybeinaccessiblemessage)
- [MessageEntity](#messageentity)
- [TextQuote](#textquote)
- [ExternalReplyInfo](#externalreplyinfo)
- [ReplyParameters](#replyparameters)
- [MessageOrigin](#messageorigin)
- [MessageOriginUser](#messageoriginuser)
- [MessageOriginHiddenUser](#messageoriginhiddenuser)
- [MessageOriginChat](#messageoriginchat)
- [MessageOriginChannel](#messageoriginchannel)
- [PhotoSize](#photosize)
- [Animation](#animation)
- [Audio](#audio)
- [Document](#document)
- [Story](#story)
- [Video](#video)
- [VideoNote](#videonote)
- [Voice](#voice)
- [PaidMediaInfo](#paidmediainfo)
- [PaidMedia](#paidmedia)
- [PaidMediaPreview](#paidmediapreview)
- [PaidMediaPhoto](#paidmediaphoto)
- [PaidMediaVideo](#paidmediavideo)
- [Contact](#contact)
- [Dice](#dice)
- [PollOption](#polloption)
- [InputPollOption](#inputpolloption)
- [PollAnswer](#pollanswer)
- [Poll](#poll)
- [Location](#location)
- [Venue](#venue)
- [WebAppData](#webappdata)
- [ProximityAlertTriggered](#proximityalerttriggered)
- [MessageAutoDeleteTimerChanged](#messageautodeletetimerchanged)
- [ChatBoostAdded](#chatboostadded)
- [BackgroundFill](#backgroundfill)
- [BackgroundFillSolid](#backgroundfillsolid)
- [BackgroundFillGradient](#backgroundfillgradient)
- [BackgroundFillFreeformGradient](#backgroundfillfreeformgradient)
- [BackgroundType](#backgroundtype)
- [BackgroundTypeFill](#backgroundtypefill)
- [BackgroundTypeWallpaper](#backgroundtypewallpaper)
- [BackgroundTypePattern](#backgroundtypepattern)
- [BackgroundTypeChatTheme](#backgroundtypechattheme)
- [ChatBackground](#chatbackground)
- [ForumTopicCreated](#forumtopiccreated)
- [ForumTopicClosed](#forumtopicclosed)
- [ForumTopicEdited](#forumtopicedited)
- [ForumTopicReopened](#forumtopicreopened)
- [GeneralForumTopicHidden](#generalforumtopichidden)
- [GeneralForumTopicUnhidden](#generalforumtopicunhidden)
- [SharedUser](#shareduser)
- [UsersShared](#usersshared)
- [ChatShared](#chatshared)
- [WriteAccessAllowed](#writeaccessallowed)
- [VideoChatScheduled](#videochatscheduled)
- [VideoChatStarted](#videochatstarted)
- [VideoChatEnded](#videochatended)
- [VideoChatParticipantsInvited](#videochatparticipantsinvited)
- [GiveawayCreated](#giveawaycreated)
- [Giveaway](#giveaway)
- [GiveawayWinners](#giveawaywinners)
- [GiveawayCompleted](#giveawaycompleted)
- [LinkPreviewOptions](#linkpreviewoptions)
- [UserProfilePhotos](#userprofilephotos)
- [File](#file)
- [WebAppInfo](#webappinfo)
- [ReplyKeyboardMarkup](#replykeyboardmarkup)
- [KeyboardButton](#keyboardbutton)
- [KeyboardButtonRequestUsers](#keyboardbuttonrequestusers)
- [KeyboardButtonRequestChat](#keyboardbuttonrequestchat)
- [KeyboardButtonPollType](#keyboardbuttonpolltype)
- [ReplyKeyboardRemove](#replykeyboardremove)
- [InlineKeyboardMarkup](#inlinekeyboardmarkup)
- [InlineKeyboardButton](#inlinekeyboardbutton)
- [LoginUrl](#loginurl)
- [SwitchInlineQueryChosenChat](#switchinlinequerychosenchat)
- [CallbackQuery](#callbackquery)
- [ForceReply](#forcereply)
- [ChatPhoto](#chatphoto)
- [ChatInviteLink](#chatinvitelink)
- [ChatAdministratorRights](#chatadministratorrights)
- [ChatMemberUpdated](#chatmemberupdated)
- [ChatMember](#chatmember)
- [ChatMemberOwner](#chatmemberowner)
- [ChatMemberAdministrator](#chatmemberadministrator)
- [ChatMemberMember](#chatmembermember)
- [ChatMemberRestricted](#chatmemberrestricted)
- [ChatMemberLeft](#chatmemberleft)
- [ChatMemberBanned](#chatmemberbanned)
- [ChatJoinRequest](#chatjoinrequest)
- [ChatPermissions](#chatpermissions)
- [Birthdate](#birthdate)
- [BusinessIntro](#businessintro)
- [BusinessLocation](#businesslocation)
- [BusinessOpeningHoursInterval](#businessopeninghoursinterval)
- [BusinessOpeningHours](#businessopeninghours)
- [ChatLocation](#chatlocation)
- [ReactionType](#reactiontype)
- [ReactionTypeEmoji](#reactiontypeemoji)
- [ReactionTypeCustomEmoji](#reactiontypecustomemoji)
- [ReactionTypePaid](#reactiontypepaid)
- [ReactionCount](#reactioncount)
- [MessageReactionUpdated](#messagereactionupdated)
- [MessageReactionCountUpdated](#messagereactioncountupdated)
- [ForumTopic](#forumtopic)
- [BotCommand](#botcommand)
- [BotCommandScope](#botcommandscope)
- [BotCommandScopeDefault](#botcommandscopedefault)
- [BotCommandScopeAllPrivateChats](#botcommandscopeallprivatechats)
- [BotCommandScopeAllGroupChats](#botcommandscopeallgroupchats)
- [BotCommandScopeAllChatAdministrators](#botcommandscopeallchatadministrators)
- [BotCommandScopeChat](#botcommandscopechat)
- [BotCommandScopeChatAdministrators](#botcommandscopechatadministrators)
- [BotCommandScopeChatMember](#botcommandscopechatmember)
- [BotName](#botname)
- [BotDescription](#botdescription)
- [BotShortDescription](#botshortdescription)
- [MenuButton](#menubutton)
- [MenuButtonCommands](#menubuttoncommands)
- [MenuButtonWebApp](#menubuttonwebapp)
- [MenuButtonDefault](#menubuttondefault)
- [ChatBoostSource](#chatboostsource)
- [ChatBoostSourcePremium](#chatboostsourcepremium)
- [ChatBoostSourceGiftCode](#chatboostsourcegiftcode)
- [ChatBoostSourceGiveaway](#chatboostsourcegiveaway)
- [ChatBoost](#chatboost)
- [ChatBoostUpdated](#chatboostupdated)
- [ChatBoostRemoved](#chatboostremoved)
- [UserChatBoosts](#userchatboosts)
- [BusinessConnection](#businessconnection)
- [BusinessMessagesDeleted](#businessmessagesdeleted)
- [ResponseParameters](#responseparameters)
- [InputMedia](#inputmedia)
- [InputMediaPhoto](#inputmediaphoto)
- [InputMediaVideo](#inputmediavideo)
- [InputMediaAnimation](#inputmediaanimation)
- [InputMediaAudio](#inputmediaaudio)
- [InputMediaDocument](#inputmediadocument)
- [InputFile](#inputfile)
- [InputPaidMedia](#inputpaidmedia)
- [InputPaidMediaPhoto](#inputpaidmediaphoto)
- [InputPaidMediaVideo](#inputpaidmediavideo)
- [Sticker](#sticker)
- [StickerSet](#stickerset)
- [MaskPosition](#maskposition)
- [InputSticker](#inputsticker)
- [InlineQuery](#inlinequery)
- [InlineQueryResultsButton](#inlinequeryresultsbutton)
- [InlineQueryResult](#inlinequeryresult)
- [InlineQueryResultArticle](#inlinequeryresultarticle)
- [InlineQueryResultPhoto](#inlinequeryresultphoto)
- [InlineQueryResultGif](#inlinequeryresultgif)
- [InlineQueryResultMpeg4Gif](#inlinequeryresultmpeg4gif)
- [InlineQueryResultVideo](#inlinequeryresultvideo)
- [InlineQueryResultAudio](#inlinequeryresultaudio)
- [InlineQueryResultVoice](#inlinequeryresultvoice)
- [InlineQueryResultDocument](#inlinequeryresultdocument)
- [InlineQueryResultLocation](#inlinequeryresultlocation)
- [InlineQueryResultVenue](#inlinequeryresultvenue)
- [InlineQueryResultContact](#inlinequeryresultcontact)
- [InlineQueryResultGame](#inlinequeryresultgame)
- [InlineQueryResultCachedPhoto](#inlinequeryresultcachedphoto)
- [InlineQueryResultCachedGif](#inlinequeryresultcachedgif)
- [InlineQueryResultCachedMpeg4Gif](#inlinequeryresultcachedmpeg4gif)
- [InlineQueryResultCachedSticker](#inlinequeryresultcachedsticker)
- [InlineQueryResultCachedDocument](#inlinequeryresultcacheddocument)
- [InlineQueryResultCachedVideo](#inlinequeryresultcachedvideo)
- [InlineQueryResultCachedVoice](#inlinequeryresultcachedvoice)
- [InlineQueryResultCachedAudio](#inlinequeryresultcachedaudio)
- [InputMessageContent](#inputmessagecontent)
- [InputTextMessageContent](#inputtextmessagecontent)
- [InputLocationMessageContent](#inputlocationmessagecontent)
- [InputVenueMessageContent](#inputvenuemessagecontent)
- [InputContactMessageContent](#inputcontactmessagecontent)
- [InputInvoiceMessageContent](#inputinvoicemessagecontent)
- [ChosenInlineResult](#choseninlineresult)
- [SentWebAppMessage](#sentwebappmessage)
- [LabeledPrice](#labeledprice)
- [Invoice](#invoice)
- [ShippingAddress](#shippingaddress)
- [OrderInfo](#orderinfo)
- [ShippingOption](#shippingoption)
- [SuccessfulPayment](#successfulpayment)
- [RefundedPayment](#refundedpayment)
- [ShippingQuery](#shippingquery)
- [PreCheckoutQuery](#precheckoutquery)
- [PaidMediaPurchased](#paidmediapurchased)
- [RevenueWithdrawalState](#revenuewithdrawalstate)
- [RevenueWithdrawalStatePending](#revenuewithdrawalstatepending)
- [RevenueWithdrawalStateSucceeded](#revenuewithdrawalstatesucceeded)
- [RevenueWithdrawalStateFailed](#revenuewithdrawalstatefailed)
- [TransactionPartner](#transactionpartner)
- [TransactionPartnerUser](#transactionpartneruser)
- [TransactionPartnerFragment](#transactionpartnerfragment)
- [TransactionPartnerTelegramAds](#transactionpartnertelegramads)
- [TransactionPartnerOther](#transactionpartnerother)
- [StarTransaction](#startransaction)
- [StarTransactions](#startransactions)
- [PassportData](#passportdata)
- [PassportFile](#passportfile)
- [EncryptedPassportElement](#encryptedpassportelement)
- [EncryptedCredentials](#encryptedcredentials)
- [PassportElementError](#passportelementerror)
- [PassportElementErrorDataField](#passportelementerrordatafield)
- [PassportElementErrorFrontSide](#passportelementerrorfrontside)
- [PassportElementErrorReverseSide](#passportelementerrorreverseside)
- [PassportElementErrorSelfie](#passportelementerrorselfie)
- [PassportElementErrorFile](#passportelementerrorfile)
- [PassportElementErrorFiles](#passportelementerrorfiles)
- [PassportElementErrorTranslationFile](#passportelementerrortranslationfile)
- [PassportElementErrorTranslationFiles](#passportelementerrortranslationfiles)
- [PassportElementErrorUnspecified](#passportelementerrorunspecified)
- [Game](#game)
- [CallbackGame](#callbackgame)
- [GameHighScore](#gamehighscore)

---
## 🚀 Methods
### ⚙️ getUpdates <a id='getupdates'></a>
- **URL**: [https://core.telegram.org/bots/api#getupdates](https://core.telegram.org/bots/api#getupdates)
- **Description**:
  - Use this method to receive incoming updates using long polling (wiki). Returns an Array of Update objects.
- **Fields**:
  - **offset**: Integer (Required: False)
    - Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates. By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as getUpdates is called with an offset higher than its update_id. The negative offset can be specified to retrieve updates starting from -offset update from the end of the updates queue. All previous updates will be forgotten.
  - **limit**: Integer (Required: False)
    - Limits the number of updates to be retrieved. Values between 1-100 are accepted. Defaults to 100.
  - **timeout**: Integer (Required: False)
    - Timeout in seconds for long polling. Defaults to 0, i.e. usual short polling. Should be positive, short polling should be used for testing purposes only.
  - **allowed_updates**: Array of String (Required: False)
    - A JSON-serialized list of the update types you want your bot to receive. For example, specify ["message", "edited_channel_post", "callback_query"] to only receive updates of these types. See Update for a complete list of available update types. Specify an empty list to receive all update types except chat_member, message_reaction, and message_reaction_count (default). If not specified, the previous setting will be used. Please note that this parameter doesn't affect updates created before the call to the getUpdates, so unwanted updates may be received for a short period of time.
- **Returns**: Array of Update

---

### ⚙️ setWebhook <a id='setwebhook'></a>
- **URL**: [https://core.telegram.org/bots/api#setwebhook](https://core.telegram.org/bots/api#setwebhook)
- **Description**:
  - Use this method to specify a URL and receive incoming updates via an outgoing webhook. Whenever there is an update for the bot, we will send an HTTPS POST request to the specified URL, containing a JSON-serialized Update. In case of an unsuccessful request, we will give up after a reasonable amount of attempts. Returns True on success.
  - If you'd like to make sure that the webhook was set by you, you can specify secret data in the parameter secret_token. If specified, the request will contain a header "X-Telegram-Bot-Api-Secret-Token" with the secret token as content.
- **Fields**:
  - **url**: String (Required: True)
    - HTTPS URL to send updates to. Use an empty string to remove webhook integration
  - **certificate**: InputFile (Required: False)
    - Upload your public key certificate so that the root certificate in use can be checked. See our self-signed guide for details.
  - **ip_address**: String (Required: False)
    - The fixed IP address which will be used to send webhook requests instead of the IP address resolved through DNS
  - **max_connections**: Integer (Required: False)
    - The maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery, 1-100. Defaults to 40. Use lower values to limit the load on your bot's server, and higher values to increase your bot's throughput.
  - **allowed_updates**: Array of String (Required: False)
    - A JSON-serialized list of the update types you want your bot to receive. For example, specify ["message", "edited_channel_post", "callback_query"] to only receive updates of these types. See Update for a complete list of available update types. Specify an empty list to receive all update types except chat_member, message_reaction, and message_reaction_count (default). If not specified, the previous setting will be used. Please note that this parameter doesn't affect updates created before the call to the setWebhook, so unwanted updates may be received for a short period of time.
  - **drop_pending_updates**: Boolean (Required: False)
    - Pass True to drop all pending updates
  - **secret_token**: String (Required: False)
    - A secret token to be sent in a header "X-Telegram-Bot-Api-Secret-Token" in every webhook request, 1-256 characters. Only characters A-Z, a-z, 0-9, _ and - are allowed. The header is useful to ensure that the request comes from a webhook set by you.
- **Returns**: Boolean

---

### ⚙️ deleteWebhook <a id='deletewebhook'></a>
- **URL**: [https://core.telegram.org/bots/api#deletewebhook](https://core.telegram.org/bots/api#deletewebhook)
- **Description**:
  - Use this method to remove webhook integration if you decide to switch back to getUpdates. Returns True on success.
- **Fields**:
  - **drop_pending_updates**: Boolean (Required: False)
    - Pass True to drop all pending updates
- **Returns**: Boolean

---

### ⚙️ getWebhookInfo <a id='getwebhookinfo'></a>
- **URL**: [https://core.telegram.org/bots/api#getwebhookinfo](https://core.telegram.org/bots/api#getwebhookinfo)
- **Description**:
  - Use this method to get current webhook status. Requires no parameters. On success, returns a WebhookInfo object. If the bot is using getUpdates, will return an object with the url field empty.
- **Returns**: WebhookInfo

---

### ⚙️ getMe <a id='getme'></a>
- **URL**: [https://core.telegram.org/bots/api#getme](https://core.telegram.org/bots/api#getme)
- **Description**:
  - A simple method for testing your bot's authentication token. Requires no parameters. Returns basic information about the bot in form of a User object.
- **Returns**: User

---

### ⚙️ logOut <a id='logout'></a>
- **URL**: [https://core.telegram.org/bots/api#logout](https://core.telegram.org/bots/api#logout)
- **Description**:
  - Use this method to log out from the cloud Bot API server before launching the bot locally. You must log out the bot before running it locally, otherwise there is no guarantee that the bot will receive updates. After a successful call, you can immediately log in on a local server, but will not be able to log in back to the cloud Bot API server for 10 minutes. Returns True on success. Requires no parameters.
- **Returns**: Boolean

---

### ⚙️ close <a id='close'></a>
- **URL**: [https://core.telegram.org/bots/api#close](https://core.telegram.org/bots/api#close)
- **Description**:
  - Use this method to close the bot instance before moving it from one local server to another. You need to delete the webhook before calling this method to ensure that the bot isn't launched again after server restart. The method will return error 429 in the first 10 minutes after the bot is launched. Returns True on success. Requires no parameters.
- **Returns**: Boolean

---

### ⚙️ sendMessage <a id='sendmessage'></a>
- **URL**: [https://core.telegram.org/bots/api#sendmessage](https://core.telegram.org/bots/api#sendmessage)
- **Description**:
  - Use this method to send text messages. On success, the sent Message is returned.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the message will be sent
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_thread_id**: Integer (Required: False)
    - Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
  - **text**: String (Required: True)
    - Text of the message to be sent, 1-4096 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Mode for parsing entities in the message text. See formatting options for more details.
  - **entities**: Array of MessageEntity (Required: False)
    - A JSON-serialized list of special entities that appear in message text, which can be specified instead of parse_mode
  - **link_preview_options**: LinkPreviewOptions (Required: False)
    - Link preview generation options for the message
  - **disable_notification**: Boolean (Required: False)
    - Sends the message silently. Users will receive a notification with no sound.
  - **protect_content**: Boolean (Required: False)
    - Protects the contents of the sent message from forwarding and saving
  - **message_effect_id**: String (Required: False)
    - Unique identifier of the message effect to be added to the message; for private chats only
  - **reply_parameters**: ReplyParameters (Required: False)
    - Description of the message to reply to
  - **reply_markup**: InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply (Required: False)
    - Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove a reply keyboard or to force a reply from the user
- **Returns**: Message

---

### ⚙️ forwardMessage <a id='forwardmessage'></a>
- **URL**: [https://core.telegram.org/bots/api#forwardmessage](https://core.telegram.org/bots/api#forwardmessage)
- **Description**:
  - Use this method to forward messages of any kind. Service messages and messages with protected content can't be forwarded. On success, the sent Message is returned.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_thread_id**: Integer (Required: False)
    - Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
  - **from_chat_id**: Integer, String (Required: True)
    - Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)
  - **disable_notification**: Boolean (Required: False)
    - Sends the message silently. Users will receive a notification with no sound.
  - **protect_content**: Boolean (Required: False)
    - Protects the contents of the forwarded message from forwarding and saving
  - **message_id**: Integer (Required: True)
    - Message identifier in the chat specified in from_chat_id
- **Returns**: Message

---

### ⚙️ forwardMessages <a id='forwardmessages'></a>
- **URL**: [https://core.telegram.org/bots/api#forwardmessages](https://core.telegram.org/bots/api#forwardmessages)
- **Description**:
  - Use this method to forward multiple messages of any kind. If some of the specified messages can't be found or forwarded, they are skipped. Service messages and messages with protected content can't be forwarded. Album grouping is kept for forwarded messages. On success, an array of MessageId of the sent messages is returned.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_thread_id**: Integer (Required: False)
    - Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
  - **from_chat_id**: Integer, String (Required: True)
    - Unique identifier for the chat where the original messages were sent (or channel username in the format @channelusername)
  - **message_ids**: Array of Integer (Required: True)
    - A JSON-serialized list of 1-100 identifiers of messages in the chat from_chat_id to forward. The identifiers must be specified in a strictly increasing order.
  - **disable_notification**: Boolean (Required: False)
    - Sends the messages silently. Users will receive a notification with no sound.
  - **protect_content**: Boolean (Required: False)
    - Protects the contents of the forwarded messages from forwarding and saving
- **Returns**: Array of MessageId

---

### ⚙️ copyMessage <a id='copymessage'></a>
- **URL**: [https://core.telegram.org/bots/api#copymessage](https://core.telegram.org/bots/api#copymessage)
- **Description**:
  - Use this method to copy messages of any kind. Service messages, paid media messages, giveaway messages, giveaway winners messages, and invoice messages can't be copied. A quiz poll can be copied only if the value of the field correct_option_id is known to the bot. The method is analogous to the method forwardMessage, but the copied message doesn't have a link to the original message. Returns the MessageId of the sent message on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_thread_id**: Integer (Required: False)
    - Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
  - **from_chat_id**: Integer, String (Required: True)
    - Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)
  - **message_id**: Integer (Required: True)
    - Message identifier in the chat specified in from_chat_id
  - **caption**: String (Required: False)
    - New caption for media, 0-1024 characters after entities parsing. If not specified, the original caption is kept
  - **parse_mode**: String (Required: False)
    - Mode for parsing entities in the new caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - A JSON-serialized list of special entities that appear in the new caption, which can be specified instead of parse_mode
  - **show_caption_above_media**: Boolean (Required: False)
    - Pass True, if the caption must be shown above the message media. Ignored if a new caption isn't specified.
  - **disable_notification**: Boolean (Required: False)
    - Sends the message silently. Users will receive a notification with no sound.
  - **protect_content**: Boolean (Required: False)
    - Protects the contents of the sent message from forwarding and saving
  - **reply_parameters**: ReplyParameters (Required: False)
    - Description of the message to reply to
  - **reply_markup**: InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply (Required: False)
    - Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove a reply keyboard or to force a reply from the user
- **Returns**: MessageId

---

### ⚙️ copyMessages <a id='copymessages'></a>
- **URL**: [https://core.telegram.org/bots/api#copymessages](https://core.telegram.org/bots/api#copymessages)
- **Description**:
  - Use this method to copy messages of any kind. If some of the specified messages can't be found or copied, they are skipped. Service messages, paid media messages, giveaway messages, giveaway winners messages, and invoice messages can't be copied. A quiz poll can be copied only if the value of the field correct_option_id is known to the bot. The method is analogous to the method forwardMessages, but the copied messages don't have a link to the original message. Album grouping is kept for copied messages. On success, an array of MessageId of the sent messages is returned.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_thread_id**: Integer (Required: False)
    - Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
  - **from_chat_id**: Integer, String (Required: True)
    - Unique identifier for the chat where the original messages were sent (or channel username in the format @channelusername)
  - **message_ids**: Array of Integer (Required: True)
    - A JSON-serialized list of 1-100 identifiers of messages in the chat from_chat_id to copy. The identifiers must be specified in a strictly increasing order.
  - **disable_notification**: Boolean (Required: False)
    - Sends the messages silently. Users will receive a notification with no sound.
  - **protect_content**: Boolean (Required: False)
    - Protects the contents of the sent messages from forwarding and saving
  - **remove_caption**: Boolean (Required: False)
    - Pass True to copy the messages without their captions
- **Returns**: Array of MessageId

---

### ⚙️ sendPhoto <a id='sendphoto'></a>
- **URL**: [https://core.telegram.org/bots/api#sendphoto](https://core.telegram.org/bots/api#sendphoto)
- **Description**:
  - Use this method to send photos. On success, the sent Message is returned.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the message will be sent
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_thread_id**: Integer (Required: False)
    - Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
  - **photo**: InputFile, String (Required: True)
    - Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data. The photo must be at most 10 MB in size. The photo's width and height must not exceed 10000 in total. Width and height ratio must be at most 20. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
  - **caption**: String (Required: False)
    - Photo caption (may also be used when resending photos by file_id), 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Mode for parsing entities in the photo caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode
  - **show_caption_above_media**: Boolean (Required: False)
    - Pass True, if the caption must be shown above the message media
  - **has_spoiler**: Boolean (Required: False)
    - Pass True if the photo needs to be covered with a spoiler animation
  - **disable_notification**: Boolean (Required: False)
    - Sends the message silently. Users will receive a notification with no sound.
  - **protect_content**: Boolean (Required: False)
    - Protects the contents of the sent message from forwarding and saving
  - **message_effect_id**: String (Required: False)
    - Unique identifier of the message effect to be added to the message; for private chats only
  - **reply_parameters**: ReplyParameters (Required: False)
    - Description of the message to reply to
  - **reply_markup**: InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply (Required: False)
    - Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove a reply keyboard or to force a reply from the user
- **Returns**: Message

---

### ⚙️ sendAudio <a id='sendaudio'></a>
- **URL**: [https://core.telegram.org/bots/api#sendaudio](https://core.telegram.org/bots/api#sendaudio)
- **Description**:
  - Use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .MP3 or .M4A format. On success, the sent Message is returned. Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future.
  - For sending voice messages, use the sendVoice method instead.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the message will be sent
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_thread_id**: Integer (Required: False)
    - Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
  - **audio**: InputFile, String (Required: True)
    - Audio file to send. Pass a file_id as String to send an audio file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an audio file from the Internet, or upload a new one using multipart/form-data. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
  - **caption**: String (Required: False)
    - Audio caption, 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Mode for parsing entities in the audio caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode
  - **duration**: Integer (Required: False)
    - Duration of the audio in seconds
  - **performer**: String (Required: False)
    - Performer
  - **title**: String (Required: False)
    - Track name
  - **thumbnail**: InputFile, String (Required: False)
    - Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
  - **disable_notification**: Boolean (Required: False)
    - Sends the message silently. Users will receive a notification with no sound.
  - **protect_content**: Boolean (Required: False)
    - Protects the contents of the sent message from forwarding and saving
  - **message_effect_id**: String (Required: False)
    - Unique identifier of the message effect to be added to the message; for private chats only
  - **reply_parameters**: ReplyParameters (Required: False)
    - Description of the message to reply to
  - **reply_markup**: InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply (Required: False)
    - Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove a reply keyboard or to force a reply from the user
- **Returns**: Message

---

### ⚙️ sendDocument <a id='senddocument'></a>
- **URL**: [https://core.telegram.org/bots/api#senddocument](https://core.telegram.org/bots/api#senddocument)
- **Description**:
  - Use this method to send general files. On success, the sent Message is returned. Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the message will be sent
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_thread_id**: Integer (Required: False)
    - Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
  - **document**: InputFile, String (Required: True)
    - File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
  - **thumbnail**: InputFile, String (Required: False)
    - Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
  - **caption**: String (Required: False)
    - Document caption (may also be used when resending documents by file_id), 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Mode for parsing entities in the document caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode
  - **disable_content_type_detection**: Boolean (Required: False)
    - Disables automatic server-side content type detection for files uploaded using multipart/form-data
  - **disable_notification**: Boolean (Required: False)
    - Sends the message silently. Users will receive a notification with no sound.
  - **protect_content**: Boolean (Required: False)
    - Protects the contents of the sent message from forwarding and saving
  - **message_effect_id**: String (Required: False)
    - Unique identifier of the message effect to be added to the message; for private chats only
  - **reply_parameters**: ReplyParameters (Required: False)
    - Description of the message to reply to
  - **reply_markup**: InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply (Required: False)
    - Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove a reply keyboard or to force a reply from the user
- **Returns**: Message

---

### ⚙️ sendVideo <a id='sendvideo'></a>
- **URL**: [https://core.telegram.org/bots/api#sendvideo](https://core.telegram.org/bots/api#sendvideo)
- **Description**:
  - Use this method to send video files, Telegram clients support MPEG4 videos (other formats may be sent as Document). On success, the sent Message is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the message will be sent
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_thread_id**: Integer (Required: False)
    - Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
  - **video**: InputFile, String (Required: True)
    - Video to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video using multipart/form-data. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
  - **duration**: Integer (Required: False)
    - Duration of sent video in seconds
  - **width**: Integer (Required: False)
    - Video width
  - **height**: Integer (Required: False)
    - Video height
  - **thumbnail**: InputFile, String (Required: False)
    - Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
  - **caption**: String (Required: False)
    - Video caption (may also be used when resending videos by file_id), 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Mode for parsing entities in the video caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode
  - **show_caption_above_media**: Boolean (Required: False)
    - Pass True, if the caption must be shown above the message media
  - **has_spoiler**: Boolean (Required: False)
    - Pass True if the video needs to be covered with a spoiler animation
  - **supports_streaming**: Boolean (Required: False)
    - Pass True if the uploaded video is suitable for streaming
  - **disable_notification**: Boolean (Required: False)
    - Sends the message silently. Users will receive a notification with no sound.
  - **protect_content**: Boolean (Required: False)
    - Protects the contents of the sent message from forwarding and saving
  - **message_effect_id**: String (Required: False)
    - Unique identifier of the message effect to be added to the message; for private chats only
  - **reply_parameters**: ReplyParameters (Required: False)
    - Description of the message to reply to
  - **reply_markup**: InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply (Required: False)
    - Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove a reply keyboard or to force a reply from the user
- **Returns**: Message

---

### ⚙️ sendAnimation <a id='sendanimation'></a>
- **URL**: [https://core.telegram.org/bots/api#sendanimation](https://core.telegram.org/bots/api#sendanimation)
- **Description**:
  - Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound). On success, the sent Message is returned. Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the message will be sent
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_thread_id**: Integer (Required: False)
    - Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
  - **animation**: InputFile, String (Required: True)
    - Animation to send. Pass a file_id as String to send an animation that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an animation from the Internet, or upload a new animation using multipart/form-data. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
  - **duration**: Integer (Required: False)
    - Duration of sent animation in seconds
  - **width**: Integer (Required: False)
    - Animation width
  - **height**: Integer (Required: False)
    - Animation height
  - **thumbnail**: InputFile, String (Required: False)
    - Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
  - **caption**: String (Required: False)
    - Animation caption (may also be used when resending animation by file_id), 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Mode for parsing entities in the animation caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode
  - **show_caption_above_media**: Boolean (Required: False)
    - Pass True, if the caption must be shown above the message media
  - **has_spoiler**: Boolean (Required: False)
    - Pass True if the animation needs to be covered with a spoiler animation
  - **disable_notification**: Boolean (Required: False)
    - Sends the message silently. Users will receive a notification with no sound.
  - **protect_content**: Boolean (Required: False)
    - Protects the contents of the sent message from forwarding and saving
  - **message_effect_id**: String (Required: False)
    - Unique identifier of the message effect to be added to the message; for private chats only
  - **reply_parameters**: ReplyParameters (Required: False)
    - Description of the message to reply to
  - **reply_markup**: InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply (Required: False)
    - Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove a reply keyboard or to force a reply from the user
- **Returns**: Message

---

### ⚙️ sendVoice <a id='sendvoice'></a>
- **URL**: [https://core.telegram.org/bots/api#sendvoice](https://core.telegram.org/bots/api#sendvoice)
- **Description**:
  - Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS, or in .MP3 format, or in .M4A format (other formats may be sent as Audio or Document). On success, the sent Message is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the message will be sent
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_thread_id**: Integer (Required: False)
    - Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
  - **voice**: InputFile, String (Required: True)
    - Audio file to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
  - **caption**: String (Required: False)
    - Voice message caption, 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Mode for parsing entities in the voice message caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode
  - **duration**: Integer (Required: False)
    - Duration of the voice message in seconds
  - **disable_notification**: Boolean (Required: False)
    - Sends the message silently. Users will receive a notification with no sound.
  - **protect_content**: Boolean (Required: False)
    - Protects the contents of the sent message from forwarding and saving
  - **message_effect_id**: String (Required: False)
    - Unique identifier of the message effect to be added to the message; for private chats only
  - **reply_parameters**: ReplyParameters (Required: False)
    - Description of the message to reply to
  - **reply_markup**: InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply (Required: False)
    - Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove a reply keyboard or to force a reply from the user
- **Returns**: Message

---

### ⚙️ sendVideoNote <a id='sendvideonote'></a>
- **URL**: [https://core.telegram.org/bots/api#sendvideonote](https://core.telegram.org/bots/api#sendvideonote)
- **Description**:
  - As of v.4.0, Telegram clients support rounded square MPEG4 videos of up to 1 minute long. Use this method to send video messages. On success, the sent Message is returned.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the message will be sent
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_thread_id**: Integer (Required: False)
    - Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
  - **video_note**: InputFile, String (Required: True)
    - Video note to send. Pass a file_id as String to send a video note that exists on the Telegram servers (recommended) or upload a new video using multipart/form-data. More information on Sending Files: https://core.telegram.org/bots/api#sending-files. Sending video notes by a URL is currently unsupported
  - **duration**: Integer (Required: False)
    - Duration of sent video in seconds
  - **length**: Integer (Required: False)
    - Video width and height, i.e. diameter of the video message
  - **thumbnail**: InputFile, String (Required: False)
    - Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
  - **disable_notification**: Boolean (Required: False)
    - Sends the message silently. Users will receive a notification with no sound.
  - **protect_content**: Boolean (Required: False)
    - Protects the contents of the sent message from forwarding and saving
  - **message_effect_id**: String (Required: False)
    - Unique identifier of the message effect to be added to the message; for private chats only
  - **reply_parameters**: ReplyParameters (Required: False)
    - Description of the message to reply to
  - **reply_markup**: InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply (Required: False)
    - Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove a reply keyboard or to force a reply from the user
- **Returns**: Message

---

### ⚙️ sendPaidMedia <a id='sendpaidmedia'></a>
- **URL**: [https://core.telegram.org/bots/api#sendpaidmedia](https://core.telegram.org/bots/api#sendpaidmedia)
- **Description**:
  - Use this method to send paid media. On success, the sent Message is returned.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the message will be sent
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername). If the chat is a channel, all Telegram Star proceeds from this media will be credited to the chat's balance. Otherwise, they will be credited to the bot's balance.
  - **star_count**: Integer (Required: True)
    - The number of Telegram Stars that must be paid to buy access to the media; 1-2500
  - **media**: Array of InputPaidMedia (Required: True)
    - A JSON-serialized array describing the media to be sent; up to 10 items
  - **payload**: String (Required: False)
    - Bot-defined paid media payload, 0-128 bytes. This will not be displayed to the user, use it for your internal processes.
  - **caption**: String (Required: False)
    - Media caption, 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Mode for parsing entities in the media caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode
  - **show_caption_above_media**: Boolean (Required: False)
    - Pass True, if the caption must be shown above the message media
  - **disable_notification**: Boolean (Required: False)
    - Sends the message silently. Users will receive a notification with no sound.
  - **protect_content**: Boolean (Required: False)
    - Protects the contents of the sent message from forwarding and saving
  - **reply_parameters**: ReplyParameters (Required: False)
    - Description of the message to reply to
  - **reply_markup**: InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply (Required: False)
    - Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove a reply keyboard or to force a reply from the user
- **Returns**: Message

---

### ⚙️ sendMediaGroup <a id='sendmediagroup'></a>
- **URL**: [https://core.telegram.org/bots/api#sendmediagroup](https://core.telegram.org/bots/api#sendmediagroup)
- **Description**:
  - Use this method to send a group of photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type. On success, an array of Messages that were sent is returned.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the message will be sent
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_thread_id**: Integer (Required: False)
    - Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
  - **media**: Array of InputMediaAudio, Array of InputMediaDocument, Array of InputMediaPhoto, Array of InputMediaVideo (Required: True)
    - A JSON-serialized array describing messages to be sent, must include 2-10 items
  - **disable_notification**: Boolean (Required: False)
    - Sends messages silently. Users will receive a notification with no sound.
  - **protect_content**: Boolean (Required: False)
    - Protects the contents of the sent messages from forwarding and saving
  - **message_effect_id**: String (Required: False)
    - Unique identifier of the message effect to be added to the message; for private chats only
  - **reply_parameters**: ReplyParameters (Required: False)
    - Description of the message to reply to
- **Returns**: Array of Message

---

### ⚙️ sendLocation <a id='sendlocation'></a>
- **URL**: [https://core.telegram.org/bots/api#sendlocation](https://core.telegram.org/bots/api#sendlocation)
- **Description**:
  - Use this method to send point on the map. On success, the sent Message is returned.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the message will be sent
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_thread_id**: Integer (Required: False)
    - Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
  - **latitude**: Float (Required: True)
    - Latitude of the location
  - **longitude**: Float (Required: True)
    - Longitude of the location
  - **horizontal_accuracy**: Float (Required: False)
    - The radius of uncertainty for the location, measured in meters; 0-1500
  - **live_period**: Integer (Required: False)
    - Period in seconds during which the location will be updated (see Live Locations, should be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely.
  - **heading**: Integer (Required: False)
    - For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
  - **proximity_alert_radius**: Integer (Required: False)
    - For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
  - **disable_notification**: Boolean (Required: False)
    - Sends the message silently. Users will receive a notification with no sound.
  - **protect_content**: Boolean (Required: False)
    - Protects the contents of the sent message from forwarding and saving
  - **message_effect_id**: String (Required: False)
    - Unique identifier of the message effect to be added to the message; for private chats only
  - **reply_parameters**: ReplyParameters (Required: False)
    - Description of the message to reply to
  - **reply_markup**: InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply (Required: False)
    - Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove a reply keyboard or to force a reply from the user
- **Returns**: Message

---

### ⚙️ sendVenue <a id='sendvenue'></a>
- **URL**: [https://core.telegram.org/bots/api#sendvenue](https://core.telegram.org/bots/api#sendvenue)
- **Description**:
  - Use this method to send information about a venue. On success, the sent Message is returned.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the message will be sent
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_thread_id**: Integer (Required: False)
    - Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
  - **latitude**: Float (Required: True)
    - Latitude of the venue
  - **longitude**: Float (Required: True)
    - Longitude of the venue
  - **title**: String (Required: True)
    - Name of the venue
  - **address**: String (Required: True)
    - Address of the venue
  - **foursquare_id**: String (Required: False)
    - Foursquare identifier of the venue
  - **foursquare_type**: String (Required: False)
    - Foursquare type of the venue, if known. (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".)
  - **google_place_id**: String (Required: False)
    - Google Places identifier of the venue
  - **google_place_type**: String (Required: False)
    - Google Places type of the venue. (See supported types.)
  - **disable_notification**: Boolean (Required: False)
    - Sends the message silently. Users will receive a notification with no sound.
  - **protect_content**: Boolean (Required: False)
    - Protects the contents of the sent message from forwarding and saving
  - **message_effect_id**: String (Required: False)
    - Unique identifier of the message effect to be added to the message; for private chats only
  - **reply_parameters**: ReplyParameters (Required: False)
    - Description of the message to reply to
  - **reply_markup**: InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply (Required: False)
    - Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove a reply keyboard or to force a reply from the user
- **Returns**: Message

---

### ⚙️ sendContact <a id='sendcontact'></a>
- **URL**: [https://core.telegram.org/bots/api#sendcontact](https://core.telegram.org/bots/api#sendcontact)
- **Description**:
  - Use this method to send phone contacts. On success, the sent Message is returned.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the message will be sent
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_thread_id**: Integer (Required: False)
    - Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
  - **phone_number**: String (Required: True)
    - Contact's phone number
  - **first_name**: String (Required: True)
    - Contact's first name
  - **last_name**: String (Required: False)
    - Contact's last name
  - **vcard**: String (Required: False)
    - Additional data about the contact in the form of a vCard, 0-2048 bytes
  - **disable_notification**: Boolean (Required: False)
    - Sends the message silently. Users will receive a notification with no sound.
  - **protect_content**: Boolean (Required: False)
    - Protects the contents of the sent message from forwarding and saving
  - **message_effect_id**: String (Required: False)
    - Unique identifier of the message effect to be added to the message; for private chats only
  - **reply_parameters**: ReplyParameters (Required: False)
    - Description of the message to reply to
  - **reply_markup**: InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply (Required: False)
    - Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove a reply keyboard or to force a reply from the user
- **Returns**: Message

---

### ⚙️ sendPoll <a id='sendpoll'></a>
- **URL**: [https://core.telegram.org/bots/api#sendpoll](https://core.telegram.org/bots/api#sendpoll)
- **Description**:
  - Use this method to send a native poll. On success, the sent Message is returned.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the message will be sent
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_thread_id**: Integer (Required: False)
    - Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
  - **question**: String (Required: True)
    - Poll question, 1-300 characters
  - **question_parse_mode**: String (Required: False)
    - Mode for parsing entities in the question. See formatting options for more details. Currently, only custom emoji entities are allowed
  - **question_entities**: Array of MessageEntity (Required: False)
    - A JSON-serialized list of special entities that appear in the poll question. It can be specified instead of question_parse_mode
  - **options**: Array of InputPollOption (Required: True)
    - A JSON-serialized list of 2-10 answer options
  - **is_anonymous**: Boolean (Required: False)
    - True, if the poll needs to be anonymous, defaults to True
  - **type**: String (Required: False)
    - Poll type, "quiz" or "regular", defaults to "regular"
  - **allows_multiple_answers**: Boolean (Required: False)
    - True, if the poll allows multiple answers, ignored for polls in quiz mode, defaults to False
  - **correct_option_id**: Integer (Required: False)
    - 0-based identifier of the correct answer option, required for polls in quiz mode
  - **explanation**: String (Required: False)
    - Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters with at most 2 line feeds after entities parsing
  - **explanation_parse_mode**: String (Required: False)
    - Mode for parsing entities in the explanation. See formatting options for more details.
  - **explanation_entities**: Array of MessageEntity (Required: False)
    - A JSON-serialized list of special entities that appear in the poll explanation. It can be specified instead of explanation_parse_mode
  - **open_period**: Integer (Required: False)
    - Amount of time in seconds the poll will be active after creation, 5-600. Can't be used together with close_date.
  - **close_date**: Integer (Required: False)
    - Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 600 seconds in the future. Can't be used together with open_period.
  - **is_closed**: Boolean (Required: False)
    - Pass True if the poll needs to be immediately closed. This can be useful for poll preview.
  - **disable_notification**: Boolean (Required: False)
    - Sends the message silently. Users will receive a notification with no sound.
  - **protect_content**: Boolean (Required: False)
    - Protects the contents of the sent message from forwarding and saving
  - **message_effect_id**: String (Required: False)
    - Unique identifier of the message effect to be added to the message; for private chats only
  - **reply_parameters**: ReplyParameters (Required: False)
    - Description of the message to reply to
  - **reply_markup**: InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply (Required: False)
    - Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove a reply keyboard or to force a reply from the user
- **Returns**: Message

---

### ⚙️ sendDice <a id='senddice'></a>
- **URL**: [https://core.telegram.org/bots/api#senddice](https://core.telegram.org/bots/api#senddice)
- **Description**:
  - Use this method to send an animated emoji that will display a random value. On success, the sent Message is returned.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the message will be sent
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_thread_id**: Integer (Required: False)
    - Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
  - **emoji**: String (Required: False)
    - Emoji on which the dice throw animation is based. Currently, must be one of "🎲", "🎯", "🏀", "⚽", "🎳", or "🎰". Dice can have values 1-6 for "🎲", "🎯" and "🎳", values 1-5 for "🏀" and "⚽", and values 1-64 for "🎰". Defaults to "🎲"
  - **disable_notification**: Boolean (Required: False)
    - Sends the message silently. Users will receive a notification with no sound.
  - **protect_content**: Boolean (Required: False)
    - Protects the contents of the sent message from forwarding
  - **message_effect_id**: String (Required: False)
    - Unique identifier of the message effect to be added to the message; for private chats only
  - **reply_parameters**: ReplyParameters (Required: False)
    - Description of the message to reply to
  - **reply_markup**: InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply (Required: False)
    - Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove a reply keyboard or to force a reply from the user
- **Returns**: Message

---

### ⚙️ sendChatAction <a id='sendchataction'></a>
- **URL**: [https://core.telegram.org/bots/api#sendchataction](https://core.telegram.org/bots/api#sendchataction)
- **Description**:
  - Use this method when you need to tell the user that something is happening on the bot's side. The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status). Returns True on success.
  - We only recommend using this method when a response from the bot will take a noticeable amount of time to arrive.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the action will be sent
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_thread_id**: Integer (Required: False)
    - Unique identifier for the target message thread; for supergroups only
  - **action**: String (Required: True)
    - Type of action to broadcast. Choose one, depending on what the user is about to receive: typing for text messages, upload_photo for photos, record_video or upload_video for videos, record_voice or upload_voice for voice notes, upload_document for general files, choose_sticker for stickers, find_location for location data, record_video_note or upload_video_note for video notes.
- **Returns**: Boolean

---

### ⚙️ setMessageReaction <a id='setmessagereaction'></a>
- **URL**: [https://core.telegram.org/bots/api#setmessagereaction](https://core.telegram.org/bots/api#setmessagereaction)
- **Description**:
  - Use this method to change the chosen reactions on a message. Service messages can't be reacted to. Automatically forwarded messages from a channel to its discussion group have the same available reactions as messages in the channel. Bots can't use paid reactions. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_id**: Integer (Required: True)
    - Identifier of the target message. If the message belongs to a media group, the reaction is set to the first non-deleted message in the group instead.
  - **reaction**: Array of ReactionType (Required: False)
    - A JSON-serialized list of reaction types to set on the message. Currently, as non-premium users, bots can set up to one reaction per message. A custom emoji reaction can be used if it is either already present on the message or explicitly allowed by chat administrators. Paid reactions can't be used by bots.
  - **is_big**: Boolean (Required: False)
    - Pass True to set the reaction with a big animation
- **Returns**: Boolean

---

### ⚙️ getUserProfilePhotos <a id='getuserprofilephotos'></a>
- **URL**: [https://core.telegram.org/bots/api#getuserprofilephotos](https://core.telegram.org/bots/api#getuserprofilephotos)
- **Description**:
  - Use this method to get a list of profile pictures for a user. Returns a UserProfilePhotos object.
- **Fields**:
  - **user_id**: Integer (Required: True)
    - Unique identifier of the target user
  - **offset**: Integer (Required: False)
    - Sequential number of the first photo to be returned. By default, all photos are returned.
  - **limit**: Integer (Required: False)
    - Limits the number of photos to be retrieved. Values between 1-100 are accepted. Defaults to 100.
- **Returns**: UserProfilePhotos

---

### ⚙️ getFile <a id='getfile'></a>
- **URL**: [https://core.telegram.org/bots/api#getfile](https://core.telegram.org/bots/api#getfile)
- **Description**:
  - Use this method to get basic information about a file and prepare it for downloading. For the moment, bots can download files of up to 20MB in size. On success, a File object is returned. The file can then be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>, where <file_path> is taken from the response. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile again.
  - Note: This function may not preserve the original file name and MIME type. You should save the file's MIME type and name (if available) when the File object is received.
- **Fields**:
  - **file_id**: String (Required: True)
    - File identifier to get information about
- **Returns**: File

---

### ⚙️ banChatMember <a id='banchatmember'></a>
- **URL**: [https://core.telegram.org/bots/api#banchatmember](https://core.telegram.org/bots/api#banchatmember)
- **Description**:
  - Use this method to ban a user in a group, a supergroup or a channel. In the case of supergroups and channels, the user will not be able to return to the chat on their own using invite links, etc., unless unbanned first. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target group or username of the target supergroup or channel (in the format @channelusername)
  - **user_id**: Integer (Required: True)
    - Unique identifier of the target user
  - **until_date**: Integer (Required: False)
    - Date when the user will be unbanned; Unix time. If user is banned for more than 366 days or less than 30 seconds from the current time they are considered to be banned forever. Applied for supergroups and channels only.
  - **revoke_messages**: Boolean (Required: False)
    - Pass True to delete all messages from the chat for the user that is being removed. If False, the user will be able to see messages in the group that were sent before the user was removed. Always True for supergroups and channels.
- **Returns**: Boolean

---

### ⚙️ unbanChatMember <a id='unbanchatmember'></a>
- **URL**: [https://core.telegram.org/bots/api#unbanchatmember](https://core.telegram.org/bots/api#unbanchatmember)
- **Description**:
  - Use this method to unban a previously banned user in a supergroup or channel. The user will not return to the group or channel automatically, but will be able to join via link, etc. The bot must be an administrator for this to work. By default, this method guarantees that after the call the user is not a member of the chat, but will be able to join it. So if the user is a member of the chat they will also be removed from the chat. If you don't want this, use the parameter only_if_banned. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target group or username of the target supergroup or channel (in the format @channelusername)
  - **user_id**: Integer (Required: True)
    - Unique identifier of the target user
  - **only_if_banned**: Boolean (Required: False)
    - Do nothing if the user is not banned
- **Returns**: Boolean

---

### ⚙️ restrictChatMember <a id='restrictchatmember'></a>
- **URL**: [https://core.telegram.org/bots/api#restrictchatmember](https://core.telegram.org/bots/api#restrictchatmember)
- **Description**:
  - Use this method to restrict a user in a supergroup. The bot must be an administrator in the supergroup for this to work and must have the appropriate administrator rights. Pass True for all permissions to lift restrictions from a user. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
  - **user_id**: Integer (Required: True)
    - Unique identifier of the target user
  - **permissions**: ChatPermissions (Required: True)
    - A JSON-serialized object for new user permissions
  - **use_independent_chat_permissions**: Boolean (Required: False)
    - Pass True if chat permissions are set independently. Otherwise, the can_send_other_messages and can_add_web_page_previews permissions will imply the can_send_messages, can_send_audios, can_send_documents, can_send_photos, can_send_videos, can_send_video_notes, and can_send_voice_notes permissions; the can_send_polls permission will imply the can_send_messages permission.
  - **until_date**: Integer (Required: False)
    - Date when restrictions will be lifted for the user; Unix time. If user is restricted for more than 366 days or less than 30 seconds from the current time, they are considered to be restricted forever
- **Returns**: Boolean

---

### ⚙️ promoteChatMember <a id='promotechatmember'></a>
- **URL**: [https://core.telegram.org/bots/api#promotechatmember](https://core.telegram.org/bots/api#promotechatmember)
- **Description**:
  - Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Pass False for all boolean parameters to demote a user. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **user_id**: Integer (Required: True)
    - Unique identifier of the target user
  - **is_anonymous**: Boolean (Required: False)
    - Pass True if the administrator's presence in the chat is hidden
  - **can_manage_chat**: Boolean (Required: False)
    - Pass True if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages and ignore slow mode. Implied by any other administrator privilege.
  - **can_delete_messages**: Boolean (Required: False)
    - Pass True if the administrator can delete messages of other users
  - **can_manage_video_chats**: Boolean (Required: False)
    - Pass True if the administrator can manage video chats
  - **can_restrict_members**: Boolean (Required: False)
    - Pass True if the administrator can restrict, ban or unban chat members, or access supergroup statistics
  - **can_promote_members**: Boolean (Required: False)
    - Pass True if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by him)
  - **can_change_info**: Boolean (Required: False)
    - Pass True if the administrator can change chat title, photo and other settings
  - **can_invite_users**: Boolean (Required: False)
    - Pass True if the administrator can invite new users to the chat
  - **can_post_stories**: Boolean (Required: False)
    - Pass True if the administrator can post stories to the chat
  - **can_edit_stories**: Boolean (Required: False)
    - Pass True if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat's story archive
  - **can_delete_stories**: Boolean (Required: False)
    - Pass True if the administrator can delete stories posted by other users
  - **can_post_messages**: Boolean (Required: False)
    - Pass True if the administrator can post messages in the channel, or access channel statistics; for channels only
  - **can_edit_messages**: Boolean (Required: False)
    - Pass True if the administrator can edit messages of other users and can pin messages; for channels only
  - **can_pin_messages**: Boolean (Required: False)
    - Pass True if the administrator can pin messages; for supergroups only
  - **can_manage_topics**: Boolean (Required: False)
    - Pass True if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only
- **Returns**: Boolean

---

### ⚙️ setChatAdministratorCustomTitle <a id='setchatadministratorcustomtitle'></a>
- **URL**: [https://core.telegram.org/bots/api#setchatadministratorcustomtitle](https://core.telegram.org/bots/api#setchatadministratorcustomtitle)
- **Description**:
  - Use this method to set a custom title for an administrator in a supergroup promoted by the bot. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
  - **user_id**: Integer (Required: True)
    - Unique identifier of the target user
  - **custom_title**: String (Required: True)
    - New custom title for the administrator; 0-16 characters, emoji are not allowed
- **Returns**: Boolean

---

### ⚙️ banChatSenderChat <a id='banchatsenderchat'></a>
- **URL**: [https://core.telegram.org/bots/api#banchatsenderchat](https://core.telegram.org/bots/api#banchatsenderchat)
- **Description**:
  - Use this method to ban a channel chat in a supergroup or a channel. Until the chat is unbanned, the owner of the banned chat won't be able to send messages on behalf of any of their channels. The bot must be an administrator in the supergroup or channel for this to work and must have the appropriate administrator rights. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **sender_chat_id**: Integer (Required: True)
    - Unique identifier of the target sender chat
- **Returns**: Boolean

---

### ⚙️ unbanChatSenderChat <a id='unbanchatsenderchat'></a>
- **URL**: [https://core.telegram.org/bots/api#unbanchatsenderchat](https://core.telegram.org/bots/api#unbanchatsenderchat)
- **Description**:
  - Use this method to unban a previously banned channel chat in a supergroup or channel. The bot must be an administrator for this to work and must have the appropriate administrator rights. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **sender_chat_id**: Integer (Required: True)
    - Unique identifier of the target sender chat
- **Returns**: Boolean

---

### ⚙️ setChatPermissions <a id='setchatpermissions'></a>
- **URL**: [https://core.telegram.org/bots/api#setchatpermissions](https://core.telegram.org/bots/api#setchatpermissions)
- **Description**:
  - Use this method to set default chat permissions for all members. The bot must be an administrator in the group or a supergroup for this to work and must have the can_restrict_members administrator rights. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
  - **permissions**: ChatPermissions (Required: True)
    - A JSON-serialized object for new default chat permissions
  - **use_independent_chat_permissions**: Boolean (Required: False)
    - Pass True if chat permissions are set independently. Otherwise, the can_send_other_messages and can_add_web_page_previews permissions will imply the can_send_messages, can_send_audios, can_send_documents, can_send_photos, can_send_videos, can_send_video_notes, and can_send_voice_notes permissions; the can_send_polls permission will imply the can_send_messages permission.
- **Returns**: Boolean

---

### ⚙️ exportChatInviteLink <a id='exportchatinvitelink'></a>
- **URL**: [https://core.telegram.org/bots/api#exportchatinvitelink](https://core.telegram.org/bots/api#exportchatinvitelink)
- **Description**:
  - Use this method to generate a new primary invite link for a chat; any previously generated primary link is revoked. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the new invite link as String on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
- **Returns**: String

---

### ⚙️ createChatInviteLink <a id='createchatinvitelink'></a>
- **URL**: [https://core.telegram.org/bots/api#createchatinvitelink](https://core.telegram.org/bots/api#createchatinvitelink)
- **Description**:
  - Use this method to create an additional invite link for a chat. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. The link can be revoked using the method revokeChatInviteLink. Returns the new invite link as ChatInviteLink object.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **name**: String (Required: False)
    - Invite link name; 0-32 characters
  - **expire_date**: Integer (Required: False)
    - Point in time (Unix timestamp) when the link will expire
  - **member_limit**: Integer (Required: False)
    - The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999
  - **creates_join_request**: Boolean (Required: False)
    - True, if users joining the chat via the link need to be approved by chat administrators. If True, member_limit can't be specified
- **Returns**: ChatInviteLink

---

### ⚙️ editChatInviteLink <a id='editchatinvitelink'></a>
- **URL**: [https://core.telegram.org/bots/api#editchatinvitelink](https://core.telegram.org/bots/api#editchatinvitelink)
- **Description**:
  - Use this method to edit a non-primary invite link created by the bot. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the edited invite link as a ChatInviteLink object.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **invite_link**: String (Required: True)
    - The invite link to edit
  - **name**: String (Required: False)
    - Invite link name; 0-32 characters
  - **expire_date**: Integer (Required: False)
    - Point in time (Unix timestamp) when the link will expire
  - **member_limit**: Integer (Required: False)
    - The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999
  - **creates_join_request**: Boolean (Required: False)
    - True, if users joining the chat via the link need to be approved by chat administrators. If True, member_limit can't be specified
- **Returns**: ChatInviteLink

---

### ⚙️ createChatSubscriptionInviteLink <a id='createchatsubscriptioninvitelink'></a>
- **URL**: [https://core.telegram.org/bots/api#createchatsubscriptioninvitelink](https://core.telegram.org/bots/api#createchatsubscriptioninvitelink)
- **Description**:
  - Use this method to create a subscription invite link for a channel chat. The bot must have the can_invite_users administrator rights. The link can be edited using the method editChatSubscriptionInviteLink or revoked using the method revokeChatInviteLink. Returns the new invite link as a ChatInviteLink object.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target channel chat or username of the target channel (in the format @channelusername)
  - **name**: String (Required: False)
    - Invite link name; 0-32 characters
  - **subscription_period**: Integer (Required: True)
    - The number of seconds the subscription will be active for before the next payment. Currently, it must always be 2592000 (30 days).
  - **subscription_price**: Integer (Required: True)
    - The amount of Telegram Stars a user must pay initially and after each subsequent subscription period to be a member of the chat; 1-2500
- **Returns**: ChatInviteLink

---

### ⚙️ editChatSubscriptionInviteLink <a id='editchatsubscriptioninvitelink'></a>
- **URL**: [https://core.telegram.org/bots/api#editchatsubscriptioninvitelink](https://core.telegram.org/bots/api#editchatsubscriptioninvitelink)
- **Description**:
  - Use this method to edit a subscription invite link created by the bot. The bot must have the can_invite_users administrator rights. Returns the edited invite link as a ChatInviteLink object.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **invite_link**: String (Required: True)
    - The invite link to edit
  - **name**: String (Required: False)
    - Invite link name; 0-32 characters
- **Returns**: ChatInviteLink

---

### ⚙️ revokeChatInviteLink <a id='revokechatinvitelink'></a>
- **URL**: [https://core.telegram.org/bots/api#revokechatinvitelink](https://core.telegram.org/bots/api#revokechatinvitelink)
- **Description**:
  - Use this method to revoke an invite link created by the bot. If the primary link is revoked, a new link is automatically generated. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the revoked invite link as ChatInviteLink object.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier of the target chat or username of the target channel (in the format @channelusername)
  - **invite_link**: String (Required: True)
    - The invite link to revoke
- **Returns**: ChatInviteLink

---

### ⚙️ approveChatJoinRequest <a id='approvechatjoinrequest'></a>
- **URL**: [https://core.telegram.org/bots/api#approvechatjoinrequest](https://core.telegram.org/bots/api#approvechatjoinrequest)
- **Description**:
  - Use this method to approve a chat join request. The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **user_id**: Integer (Required: True)
    - Unique identifier of the target user
- **Returns**: Boolean

---

### ⚙️ declineChatJoinRequest <a id='declinechatjoinrequest'></a>
- **URL**: [https://core.telegram.org/bots/api#declinechatjoinrequest](https://core.telegram.org/bots/api#declinechatjoinrequest)
- **Description**:
  - Use this method to decline a chat join request. The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **user_id**: Integer (Required: True)
    - Unique identifier of the target user
- **Returns**: Boolean

---

### ⚙️ setChatPhoto <a id='setchatphoto'></a>
- **URL**: [https://core.telegram.org/bots/api#setchatphoto](https://core.telegram.org/bots/api#setchatphoto)
- **Description**:
  - Use this method to set a new profile photo for the chat. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **photo**: InputFile (Required: True)
    - New chat photo, uploaded using multipart/form-data
- **Returns**: Boolean

---

### ⚙️ deleteChatPhoto <a id='deletechatphoto'></a>
- **URL**: [https://core.telegram.org/bots/api#deletechatphoto](https://core.telegram.org/bots/api#deletechatphoto)
- **Description**:
  - Use this method to delete a chat photo. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
- **Returns**: Boolean

---

### ⚙️ setChatTitle <a id='setchattitle'></a>
- **URL**: [https://core.telegram.org/bots/api#setchattitle](https://core.telegram.org/bots/api#setchattitle)
- **Description**:
  - Use this method to change the title of a chat. Titles can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **title**: String (Required: True)
    - New chat title, 1-128 characters
- **Returns**: Boolean

---

### ⚙️ setChatDescription <a id='setchatdescription'></a>
- **URL**: [https://core.telegram.org/bots/api#setchatdescription](https://core.telegram.org/bots/api#setchatdescription)
- **Description**:
  - Use this method to change the description of a group, a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **description**: String (Required: False)
    - New chat description, 0-255 characters
- **Returns**: Boolean

---

### ⚙️ pinChatMessage <a id='pinchatmessage'></a>
- **URL**: [https://core.telegram.org/bots/api#pinchatmessage](https://core.telegram.org/bots/api#pinchatmessage)
- **Description**:
  - Use this method to add a message to the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the message will be pinned
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_id**: Integer (Required: True)
    - Identifier of a message to pin
  - **disable_notification**: Boolean (Required: False)
    - Pass True if it is not necessary to send a notification to all chat members about the new pinned message. Notifications are always disabled in channels and private chats.
- **Returns**: Boolean

---

### ⚙️ unpinChatMessage <a id='unpinchatmessage'></a>
- **URL**: [https://core.telegram.org/bots/api#unpinchatmessage](https://core.telegram.org/bots/api#unpinchatmessage)
- **Description**:
  - Use this method to remove a message from the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the message will be unpinned
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_id**: Integer (Required: False)
    - Identifier of the message to unpin. Required if business_connection_id is specified. If not specified, the most recent pinned message (by sending date) will be unpinned.
- **Returns**: Boolean

---

### ⚙️ unpinAllChatMessages <a id='unpinallchatmessages'></a>
- **URL**: [https://core.telegram.org/bots/api#unpinallchatmessages](https://core.telegram.org/bots/api#unpinallchatmessages)
- **Description**:
  - Use this method to clear the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
- **Returns**: Boolean

---

### ⚙️ leaveChat <a id='leavechat'></a>
- **URL**: [https://core.telegram.org/bots/api#leavechat](https://core.telegram.org/bots/api#leavechat)
- **Description**:
  - Use this method for your bot to leave a group, supergroup or channel. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
- **Returns**: Boolean

---

### ⚙️ getChat <a id='getchat'></a>
- **URL**: [https://core.telegram.org/bots/api#getchat](https://core.telegram.org/bots/api#getchat)
- **Description**:
  - Use this method to get up-to-date information about the chat. Returns a ChatFullInfo object on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
- **Returns**: ChatFullInfo

---

### ⚙️ getChatAdministrators <a id='getchatadministrators'></a>
- **URL**: [https://core.telegram.org/bots/api#getchatadministrators](https://core.telegram.org/bots/api#getchatadministrators)
- **Description**:
  - Use this method to get a list of administrators in a chat, which aren't bots. Returns an Array of ChatMember objects.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
- **Returns**: Array of ChatMember

---

### ⚙️ getChatMemberCount <a id='getchatmembercount'></a>
- **URL**: [https://core.telegram.org/bots/api#getchatmembercount](https://core.telegram.org/bots/api#getchatmembercount)
- **Description**:
  - Use this method to get the number of members in a chat. Returns Int on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
- **Returns**: Integer

---

### ⚙️ getChatMember <a id='getchatmember'></a>
- **URL**: [https://core.telegram.org/bots/api#getchatmember](https://core.telegram.org/bots/api#getchatmember)
- **Description**:
  - Use this method to get information about a member of a chat. The method is only guaranteed to work for other users if the bot is an administrator in the chat. Returns a ChatMember object on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
  - **user_id**: Integer (Required: True)
    - Unique identifier of the target user
- **Returns**: ChatMember

---

### ⚙️ setChatStickerSet <a id='setchatstickerset'></a>
- **URL**: [https://core.telegram.org/bots/api#setchatstickerset](https://core.telegram.org/bots/api#setchatstickerset)
- **Description**:
  - Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
  - **sticker_set_name**: String (Required: True)
    - Name of the sticker set to be set as the group sticker set
- **Returns**: Boolean

---

### ⚙️ deleteChatStickerSet <a id='deletechatstickerset'></a>
- **URL**: [https://core.telegram.org/bots/api#deletechatstickerset](https://core.telegram.org/bots/api#deletechatstickerset)
- **Description**:
  - Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
- **Returns**: Boolean

---

### ⚙️ getForumTopicIconStickers <a id='getforumtopiciconstickers'></a>
- **URL**: [https://core.telegram.org/bots/api#getforumtopiciconstickers](https://core.telegram.org/bots/api#getforumtopiciconstickers)
- **Description**:
  - Use this method to get custom emoji stickers, which can be used as a forum topic icon by any user. Requires no parameters. Returns an Array of Sticker objects.
- **Returns**: Array of Sticker

---

### ⚙️ createForumTopic <a id='createforumtopic'></a>
- **URL**: [https://core.telegram.org/bots/api#createforumtopic](https://core.telegram.org/bots/api#createforumtopic)
- **Description**:
  - Use this method to create a topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. Returns information about the created topic as a ForumTopic object.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
  - **name**: String (Required: True)
    - Topic name, 1-128 characters
  - **icon_color**: Integer (Required: False)
    - Color of the topic icon in RGB format. Currently, must be one of 7322096 (0x6FB9F0), 16766590 (0xFFD67E), 13338331 (0xCB86DB), 9367192 (0x8EEE98), 16749490 (0xFF93B2), or 16478047 (0xFB6F5F)
  - **icon_custom_emoji_id**: String (Required: False)
    - Unique identifier of the custom emoji shown as the topic icon. Use getForumTopicIconStickers to get all allowed custom emoji identifiers.
- **Returns**: ForumTopic

---

### ⚙️ editForumTopic <a id='editforumtopic'></a>
- **URL**: [https://core.telegram.org/bots/api#editforumtopic](https://core.telegram.org/bots/api#editforumtopic)
- **Description**:
  - Use this method to edit name and icon of a topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights, unless it is the creator of the topic. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
  - **message_thread_id**: Integer (Required: True)
    - Unique identifier for the target message thread of the forum topic
  - **name**: String (Required: False)
    - New topic name, 0-128 characters. If not specified or empty, the current name of the topic will be kept
  - **icon_custom_emoji_id**: String (Required: False)
    - New unique identifier of the custom emoji shown as the topic icon. Use getForumTopicIconStickers to get all allowed custom emoji identifiers. Pass an empty string to remove the icon. If not specified, the current icon will be kept
- **Returns**: Boolean

---

### ⚙️ closeForumTopic <a id='closeforumtopic'></a>
- **URL**: [https://core.telegram.org/bots/api#closeforumtopic](https://core.telegram.org/bots/api#closeforumtopic)
- **Description**:
  - Use this method to close an open topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights, unless it is the creator of the topic. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
  - **message_thread_id**: Integer (Required: True)
    - Unique identifier for the target message thread of the forum topic
- **Returns**: Boolean

---

### ⚙️ reopenForumTopic <a id='reopenforumtopic'></a>
- **URL**: [https://core.telegram.org/bots/api#reopenforumtopic](https://core.telegram.org/bots/api#reopenforumtopic)
- **Description**:
  - Use this method to reopen a closed topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights, unless it is the creator of the topic. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
  - **message_thread_id**: Integer (Required: True)
    - Unique identifier for the target message thread of the forum topic
- **Returns**: Boolean

---

### ⚙️ deleteForumTopic <a id='deleteforumtopic'></a>
- **URL**: [https://core.telegram.org/bots/api#deleteforumtopic](https://core.telegram.org/bots/api#deleteforumtopic)
- **Description**:
  - Use this method to delete a forum topic along with all its messages in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_delete_messages administrator rights. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
  - **message_thread_id**: Integer (Required: True)
    - Unique identifier for the target message thread of the forum topic
- **Returns**: Boolean

---

### ⚙️ unpinAllForumTopicMessages <a id='unpinallforumtopicmessages'></a>
- **URL**: [https://core.telegram.org/bots/api#unpinallforumtopicmessages](https://core.telegram.org/bots/api#unpinallforumtopicmessages)
- **Description**:
  - Use this method to clear the list of pinned messages in a forum topic. The bot must be an administrator in the chat for this to work and must have the can_pin_messages administrator right in the supergroup. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
  - **message_thread_id**: Integer (Required: True)
    - Unique identifier for the target message thread of the forum topic
- **Returns**: Boolean

---

### ⚙️ editGeneralForumTopic <a id='editgeneralforumtopic'></a>
- **URL**: [https://core.telegram.org/bots/api#editgeneralforumtopic](https://core.telegram.org/bots/api#editgeneralforumtopic)
- **Description**:
  - Use this method to edit the name of the 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
  - **name**: String (Required: True)
    - New topic name, 1-128 characters
- **Returns**: Boolean

---

### ⚙️ closeGeneralForumTopic <a id='closegeneralforumtopic'></a>
- **URL**: [https://core.telegram.org/bots/api#closegeneralforumtopic](https://core.telegram.org/bots/api#closegeneralforumtopic)
- **Description**:
  - Use this method to close an open 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
- **Returns**: Boolean

---

### ⚙️ reopenGeneralForumTopic <a id='reopengeneralforumtopic'></a>
- **URL**: [https://core.telegram.org/bots/api#reopengeneralforumtopic](https://core.telegram.org/bots/api#reopengeneralforumtopic)
- **Description**:
  - Use this method to reopen a closed 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. The topic will be automatically unhidden if it was hidden. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
- **Returns**: Boolean

---

### ⚙️ hideGeneralForumTopic <a id='hidegeneralforumtopic'></a>
- **URL**: [https://core.telegram.org/bots/api#hidegeneralforumtopic](https://core.telegram.org/bots/api#hidegeneralforumtopic)
- **Description**:
  - Use this method to hide the 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. The topic will be automatically closed if it was open. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
- **Returns**: Boolean

---

### ⚙️ unhideGeneralForumTopic <a id='unhidegeneralforumtopic'></a>
- **URL**: [https://core.telegram.org/bots/api#unhidegeneralforumtopic](https://core.telegram.org/bots/api#unhidegeneralforumtopic)
- **Description**:
  - Use this method to unhide the 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
- **Returns**: Boolean

---

### ⚙️ unpinAllGeneralForumTopicMessages <a id='unpinallgeneralforumtopicmessages'></a>
- **URL**: [https://core.telegram.org/bots/api#unpinallgeneralforumtopicmessages](https://core.telegram.org/bots/api#unpinallgeneralforumtopicmessages)
- **Description**:
  - Use this method to clear the list of pinned messages in a General forum topic. The bot must be an administrator in the chat for this to work and must have the can_pin_messages administrator right in the supergroup. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
- **Returns**: Boolean

---

### ⚙️ answerCallbackQuery <a id='answercallbackquery'></a>
- **URL**: [https://core.telegram.org/bots/api#answercallbackquery](https://core.telegram.org/bots/api#answercallbackquery)
- **Description**:
  - Use this method to send answers to callback queries sent from inline keyboards. The answer will be displayed to the user as a notification at the top of the chat screen or as an alert. On success, True is returned.
- **Fields**:
  - **callback_query_id**: String (Required: True)
    - Unique identifier for the query to be answered
  - **text**: String (Required: False)
    - Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters
  - **show_alert**: Boolean (Required: False)
    - If True, an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to false.
  - **url**: String (Required: False)
    - URL that will be opened by the user's client. If you have created a Game and accepted the conditions via @BotFather, specify the URL that opens your game - note that this will only work if the query comes from a callback_game button. Otherwise, you may use links like t.me/your_bot?start=XXXX that open your bot with a parameter.
  - **cache_time**: Integer (Required: False)
    - The maximum amount of time in seconds that the result of the callback query may be cached client-side. Telegram apps will support caching starting in version 3.14. Defaults to 0.
- **Returns**: Boolean

---

### ⚙️ getUserChatBoosts <a id='getuserchatboosts'></a>
- **URL**: [https://core.telegram.org/bots/api#getuserchatboosts](https://core.telegram.org/bots/api#getuserchatboosts)
- **Description**:
  - Use this method to get the list of boosts added to a chat by a user. Requires administrator rights in the chat. Returns a UserChatBoosts object.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the chat or username of the channel (in the format @channelusername)
  - **user_id**: Integer (Required: True)
    - Unique identifier of the target user
- **Returns**: UserChatBoosts

---

### ⚙️ getBusinessConnection <a id='getbusinessconnection'></a>
- **URL**: [https://core.telegram.org/bots/api#getbusinessconnection](https://core.telegram.org/bots/api#getbusinessconnection)
- **Description**:
  - Use this method to get information about the connection of the bot with a business account. Returns a BusinessConnection object on success.
- **Fields**:
  - **business_connection_id**: String (Required: True)
    - Unique identifier of the business connection
- **Returns**: BusinessConnection

---

### ⚙️ setMyCommands <a id='setmycommands'></a>
- **URL**: [https://core.telegram.org/bots/api#setmycommands](https://core.telegram.org/bots/api#setmycommands)
- **Description**:
  - Use this method to change the list of the bot's commands. See this manual for more details about bot commands. Returns True on success.
- **Fields**:
  - **commands**: Array of BotCommand (Required: True)
    - A JSON-serialized list of bot commands to be set as the list of the bot's commands. At most 100 commands can be specified.
  - **scope**: BotCommandScope (Required: False)
    - A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to BotCommandScopeDefault.
  - **language_code**: String (Required: False)
    - A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands
- **Returns**: Boolean

---

### ⚙️ deleteMyCommands <a id='deletemycommands'></a>
- **URL**: [https://core.telegram.org/bots/api#deletemycommands](https://core.telegram.org/bots/api#deletemycommands)
- **Description**:
  - Use this method to delete the list of the bot's commands for the given scope and user language. After deletion, higher level commands will be shown to affected users. Returns True on success.
- **Fields**:
  - **scope**: BotCommandScope (Required: False)
    - A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to BotCommandScopeDefault.
  - **language_code**: String (Required: False)
    - A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands
- **Returns**: Boolean

---

### ⚙️ getMyCommands <a id='getmycommands'></a>
- **URL**: [https://core.telegram.org/bots/api#getmycommands](https://core.telegram.org/bots/api#getmycommands)
- **Description**:
  - Use this method to get the current list of the bot's commands for the given scope and user language. Returns an Array of BotCommand objects. If commands aren't set, an empty list is returned.
- **Fields**:
  - **scope**: BotCommandScope (Required: False)
    - A JSON-serialized object, describing scope of users. Defaults to BotCommandScopeDefault.
  - **language_code**: String (Required: False)
    - A two-letter ISO 639-1 language code or an empty string
- **Returns**: Array of BotCommand

---

### ⚙️ setMyName <a id='setmyname'></a>
- **URL**: [https://core.telegram.org/bots/api#setmyname](https://core.telegram.org/bots/api#setmyname)
- **Description**:
  - Use this method to change the bot's name. Returns True on success.
- **Fields**:
  - **name**: String (Required: False)
    - New bot name; 0-64 characters. Pass an empty string to remove the dedicated name for the given language.
  - **language_code**: String (Required: False)
    - A two-letter ISO 639-1 language code. If empty, the name will be shown to all users for whose language there is no dedicated name.
- **Returns**: Boolean

---

### ⚙️ getMyName <a id='getmyname'></a>
- **URL**: [https://core.telegram.org/bots/api#getmyname](https://core.telegram.org/bots/api#getmyname)
- **Description**:
  - Use this method to get the current bot name for the given user language. Returns BotName on success.
- **Fields**:
  - **language_code**: String (Required: False)
    - A two-letter ISO 639-1 language code or an empty string
- **Returns**: BotName

---

### ⚙️ setMyDescription <a id='setmydescription'></a>
- **URL**: [https://core.telegram.org/bots/api#setmydescription](https://core.telegram.org/bots/api#setmydescription)
- **Description**:
  - Use this method to change the bot's description, which is shown in the chat with the bot if the chat is empty. Returns True on success.
- **Fields**:
  - **description**: String (Required: False)
    - New bot description; 0-512 characters. Pass an empty string to remove the dedicated description for the given language.
  - **language_code**: String (Required: False)
    - A two-letter ISO 639-1 language code. If empty, the description will be applied to all users for whose language there is no dedicated description.
- **Returns**: Boolean

---

### ⚙️ getMyDescription <a id='getmydescription'></a>
- **URL**: [https://core.telegram.org/bots/api#getmydescription](https://core.telegram.org/bots/api#getmydescription)
- **Description**:
  - Use this method to get the current bot description for the given user language. Returns BotDescription on success.
- **Fields**:
  - **language_code**: String (Required: False)
    - A two-letter ISO 639-1 language code or an empty string
- **Returns**: BotDescription

---

### ⚙️ setMyShortDescription <a id='setmyshortdescription'></a>
- **URL**: [https://core.telegram.org/bots/api#setmyshortdescription](https://core.telegram.org/bots/api#setmyshortdescription)
- **Description**:
  - Use this method to change the bot's short description, which is shown on the bot's profile page and is sent together with the link when users share the bot. Returns True on success.
- **Fields**:
  - **short_description**: String (Required: False)
    - New short description for the bot; 0-120 characters. Pass an empty string to remove the dedicated short description for the given language.
  - **language_code**: String (Required: False)
    - A two-letter ISO 639-1 language code. If empty, the short description will be applied to all users for whose language there is no dedicated short description.
- **Returns**: Boolean

---

### ⚙️ getMyShortDescription <a id='getmyshortdescription'></a>
- **URL**: [https://core.telegram.org/bots/api#getmyshortdescription](https://core.telegram.org/bots/api#getmyshortdescription)
- **Description**:
  - Use this method to get the current bot short description for the given user language. Returns BotShortDescription on success.
- **Fields**:
  - **language_code**: String (Required: False)
    - A two-letter ISO 639-1 language code or an empty string
- **Returns**: BotShortDescription

---

### ⚙️ setChatMenuButton <a id='setchatmenubutton'></a>
- **URL**: [https://core.telegram.org/bots/api#setchatmenubutton](https://core.telegram.org/bots/api#setchatmenubutton)
- **Description**:
  - Use this method to change the bot's menu button in a private chat, or the default menu button. Returns True on success.
- **Fields**:
  - **chat_id**: Integer (Required: False)
    - Unique identifier for the target private chat. If not specified, default bot's menu button will be changed
  - **menu_button**: MenuButton (Required: False)
    - A JSON-serialized object for the bot's new menu button. Defaults to MenuButtonDefault
- **Returns**: Boolean

---

### ⚙️ getChatMenuButton <a id='getchatmenubutton'></a>
- **URL**: [https://core.telegram.org/bots/api#getchatmenubutton](https://core.telegram.org/bots/api#getchatmenubutton)
- **Description**:
  - Use this method to get the current value of the bot's menu button in a private chat, or the default menu button. Returns MenuButton on success.
- **Fields**:
  - **chat_id**: Integer (Required: False)
    - Unique identifier for the target private chat. If not specified, default bot's menu button will be returned
- **Returns**: MenuButton

---

### ⚙️ setMyDefaultAdministratorRights <a id='setmydefaultadministratorrights'></a>
- **URL**: [https://core.telegram.org/bots/api#setmydefaultadministratorrights](https://core.telegram.org/bots/api#setmydefaultadministratorrights)
- **Description**:
  - Use this method to change the default administrator rights requested by the bot when it's added as an administrator to groups or channels. These rights will be suggested to users, but they are free to modify the list before adding the bot. Returns True on success.
- **Fields**:
  - **rights**: ChatAdministratorRights (Required: False)
    - A JSON-serialized object describing new default administrator rights. If not specified, the default administrator rights will be cleared.
  - **for_channels**: Boolean (Required: False)
    - Pass True to change the default administrator rights of the bot in channels. Otherwise, the default administrator rights of the bot for groups and supergroups will be changed.
- **Returns**: Boolean

---

### ⚙️ getMyDefaultAdministratorRights <a id='getmydefaultadministratorrights'></a>
- **URL**: [https://core.telegram.org/bots/api#getmydefaultadministratorrights](https://core.telegram.org/bots/api#getmydefaultadministratorrights)
- **Description**:
  - Use this method to get the current default administrator rights of the bot. Returns ChatAdministratorRights on success.
- **Fields**:
  - **for_channels**: Boolean (Required: False)
    - Pass True to get default administrator rights of the bot in channels. Otherwise, default administrator rights of the bot for groups and supergroups will be returned.
- **Returns**: ChatAdministratorRights

---

### ⚙️ editMessageText <a id='editmessagetext'></a>
- **URL**: [https://core.telegram.org/bots/api#editmessagetext](https://core.telegram.org/bots/api#editmessagetext)
- **Description**:
  - Use this method to edit text and game messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within 48 hours from the time they were sent.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the message to be edited was sent
  - **chat_id**: Integer, String (Required: False)
    - Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_id**: Integer (Required: False)
    - Required if inline_message_id is not specified. Identifier of the message to edit
  - **inline_message_id**: String (Required: False)
    - Required if chat_id and message_id are not specified. Identifier of the inline message
  - **text**: String (Required: True)
    - New text of the message, 1-4096 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Mode for parsing entities in the message text. See formatting options for more details.
  - **entities**: Array of MessageEntity (Required: False)
    - A JSON-serialized list of special entities that appear in message text, which can be specified instead of parse_mode
  - **link_preview_options**: LinkPreviewOptions (Required: False)
    - Link preview generation options for the message
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - A JSON-serialized object for an inline keyboard.
- **Returns**: Message, Boolean

---

### ⚙️ editMessageCaption <a id='editmessagecaption'></a>
- **URL**: [https://core.telegram.org/bots/api#editmessagecaption](https://core.telegram.org/bots/api#editmessagecaption)
- **Description**:
  - Use this method to edit captions of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within 48 hours from the time they were sent.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the message to be edited was sent
  - **chat_id**: Integer, String (Required: False)
    - Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_id**: Integer (Required: False)
    - Required if inline_message_id is not specified. Identifier of the message to edit
  - **inline_message_id**: String (Required: False)
    - Required if chat_id and message_id are not specified. Identifier of the inline message
  - **caption**: String (Required: False)
    - New caption of the message, 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Mode for parsing entities in the message caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode
  - **show_caption_above_media**: Boolean (Required: False)
    - Pass True, if the caption must be shown above the message media. Supported only for animation, photo and video messages.
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - A JSON-serialized object for an inline keyboard.
- **Returns**: Message, Boolean

---

### ⚙️ editMessageMedia <a id='editmessagemedia'></a>
- **URL**: [https://core.telegram.org/bots/api#editmessagemedia](https://core.telegram.org/bots/api#editmessagemedia)
- **Description**:
  - Use this method to edit animation, audio, document, photo, or video messages. If a message is part of a message album, then it can be edited only to an audio for audio albums, only to a document for document albums and to a photo or a video otherwise. When an inline message is edited, a new file can't be uploaded; use a previously uploaded file via its file_id or specify a URL. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within 48 hours from the time they were sent.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the message to be edited was sent
  - **chat_id**: Integer, String (Required: False)
    - Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_id**: Integer (Required: False)
    - Required if inline_message_id is not specified. Identifier of the message to edit
  - **inline_message_id**: String (Required: False)
    - Required if chat_id and message_id are not specified. Identifier of the inline message
  - **media**: InputMedia (Required: True)
    - A JSON-serialized object for a new media content of the message
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - A JSON-serialized object for a new inline keyboard.
- **Returns**: Message, Boolean

---

### ⚙️ editMessageLiveLocation <a id='editmessagelivelocation'></a>
- **URL**: [https://core.telegram.org/bots/api#editmessagelivelocation](https://core.telegram.org/bots/api#editmessagelivelocation)
- **Description**:
  - Use this method to edit live location messages. A location can be edited until its live_period expires or editing is explicitly disabled by a call to stopMessageLiveLocation. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the message to be edited was sent
  - **chat_id**: Integer, String (Required: False)
    - Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_id**: Integer (Required: False)
    - Required if inline_message_id is not specified. Identifier of the message to edit
  - **inline_message_id**: String (Required: False)
    - Required if chat_id and message_id are not specified. Identifier of the inline message
  - **latitude**: Float (Required: True)
    - Latitude of new location
  - **longitude**: Float (Required: True)
    - Longitude of new location
  - **live_period**: Integer (Required: False)
    - New period in seconds during which the location can be updated, starting from the message send date. If 0x7FFFFFFF is specified, then the location can be updated forever. Otherwise, the new value must not exceed the current live_period by more than a day, and the live location expiration date must remain within the next 90 days. If not specified, then live_period remains unchanged
  - **horizontal_accuracy**: Float (Required: False)
    - The radius of uncertainty for the location, measured in meters; 0-1500
  - **heading**: Integer (Required: False)
    - Direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
  - **proximity_alert_radius**: Integer (Required: False)
    - The maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - A JSON-serialized object for a new inline keyboard.
- **Returns**: Message, Boolean

---

### ⚙️ stopMessageLiveLocation <a id='stopmessagelivelocation'></a>
- **URL**: [https://core.telegram.org/bots/api#stopmessagelivelocation](https://core.telegram.org/bots/api#stopmessagelivelocation)
- **Description**:
  - Use this method to stop updating a live location message before live_period expires. On success, if the message is not an inline message, the edited Message is returned, otherwise True is returned.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the message to be edited was sent
  - **chat_id**: Integer, String (Required: False)
    - Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_id**: Integer (Required: False)
    - Required if inline_message_id is not specified. Identifier of the message with live location to stop
  - **inline_message_id**: String (Required: False)
    - Required if chat_id and message_id are not specified. Identifier of the inline message
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - A JSON-serialized object for a new inline keyboard.
- **Returns**: Message, Boolean

---

### ⚙️ editMessageReplyMarkup <a id='editmessagereplymarkup'></a>
- **URL**: [https://core.telegram.org/bots/api#editmessagereplymarkup](https://core.telegram.org/bots/api#editmessagereplymarkup)
- **Description**:
  - Use this method to edit only the reply markup of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within 48 hours from the time they were sent.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the message to be edited was sent
  - **chat_id**: Integer, String (Required: False)
    - Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_id**: Integer (Required: False)
    - Required if inline_message_id is not specified. Identifier of the message to edit
  - **inline_message_id**: String (Required: False)
    - Required if chat_id and message_id are not specified. Identifier of the inline message
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - A JSON-serialized object for an inline keyboard.
- **Returns**: Message, Boolean

---

### ⚙️ stopPoll <a id='stoppoll'></a>
- **URL**: [https://core.telegram.org/bots/api#stoppoll](https://core.telegram.org/bots/api#stoppoll)
- **Description**:
  - Use this method to stop a poll which was sent by the bot. On success, the stopped Poll is returned.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the message to be edited was sent
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_id**: Integer (Required: True)
    - Identifier of the original message with the poll
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - A JSON-serialized object for a new message inline keyboard.
- **Returns**: Poll

---

### ⚙️ deleteMessage <a id='deletemessage'></a>
- **URL**: [https://core.telegram.org/bots/api#deletemessage](https://core.telegram.org/bots/api#deletemessage)
- **Description**:
  - Use this method to delete a message, including service messages, with the following limitations:
  - - A message can only be deleted if it was sent less than 48 hours ago.
  - - Service messages about a supergroup, channel, or forum topic creation can't be deleted.
  - - A dice message in a private chat can only be deleted if it was sent more than 24 hours ago.
  - - Bots can delete outgoing messages in private chats, groups, and supergroups.
  - - Bots can delete incoming messages in private chats.
  - - Bots granted can_post_messages permissions can delete outgoing messages in channels.
  - - If the bot is an administrator of a group, it can delete any message there.
  - - If the bot has can_delete_messages permission in a supergroup or a channel, it can delete any message there.
  - Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_id**: Integer (Required: True)
    - Identifier of the message to delete
- **Returns**: Boolean

---

### ⚙️ deleteMessages <a id='deletemessages'></a>
- **URL**: [https://core.telegram.org/bots/api#deletemessages](https://core.telegram.org/bots/api#deletemessages)
- **Description**:
  - Use this method to delete multiple messages simultaneously. If some of the specified messages can't be found, they are skipped. Returns True on success.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_ids**: Array of Integer (Required: True)
    - A JSON-serialized list of 1-100 identifiers of messages to delete. See deleteMessage for limitations on which messages can be deleted
- **Returns**: Boolean

---

### ⚙️ sendSticker <a id='sendsticker'></a>
- **URL**: [https://core.telegram.org/bots/api#sendsticker](https://core.telegram.org/bots/api#sendsticker)
- **Description**:
  - Use this method to send static .WEBP, animated .TGS, or video .WEBM stickers. On success, the sent Message is returned.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the message will be sent
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_thread_id**: Integer (Required: False)
    - Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
  - **sticker**: InputFile, String (Required: True)
    - Sticker to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a .WEBP sticker from the Internet, or upload a new .WEBP, .TGS, or .WEBM sticker using multipart/form-data. More information on Sending Files: https://core.telegram.org/bots/api#sending-files. Video and animated stickers can't be sent via an HTTP URL.
  - **emoji**: String (Required: False)
    - Emoji associated with the sticker; only for just uploaded stickers
  - **disable_notification**: Boolean (Required: False)
    - Sends the message silently. Users will receive a notification with no sound.
  - **protect_content**: Boolean (Required: False)
    - Protects the contents of the sent message from forwarding and saving
  - **message_effect_id**: String (Required: False)
    - Unique identifier of the message effect to be added to the message; for private chats only
  - **reply_parameters**: ReplyParameters (Required: False)
    - Description of the message to reply to
  - **reply_markup**: InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply (Required: False)
    - Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove a reply keyboard or to force a reply from the user
- **Returns**: Message

---

### ⚙️ getStickerSet <a id='getstickerset'></a>
- **URL**: [https://core.telegram.org/bots/api#getstickerset](https://core.telegram.org/bots/api#getstickerset)
- **Description**:
  - Use this method to get a sticker set. On success, a StickerSet object is returned.
- **Fields**:
  - **name**: String (Required: True)
    - Name of the sticker set
- **Returns**: StickerSet

---

### ⚙️ getCustomEmojiStickers <a id='getcustomemojistickers'></a>
- **URL**: [https://core.telegram.org/bots/api#getcustomemojistickers](https://core.telegram.org/bots/api#getcustomemojistickers)
- **Description**:
  - Use this method to get information about custom emoji stickers by their identifiers. Returns an Array of Sticker objects.
- **Fields**:
  - **custom_emoji_ids**: Array of String (Required: True)
    - A JSON-serialized list of custom emoji identifiers. At most 200 custom emoji identifiers can be specified.
- **Returns**: Array of Sticker

---

### ⚙️ uploadStickerFile <a id='uploadstickerfile'></a>
- **URL**: [https://core.telegram.org/bots/api#uploadstickerfile](https://core.telegram.org/bots/api#uploadstickerfile)
- **Description**:
  - Use this method to upload a file with a sticker for later use in the createNewStickerSet, addStickerToSet, or replaceStickerInSet methods (the file can be used multiple times). Returns the uploaded File on success.
- **Fields**:
  - **user_id**: Integer (Required: True)
    - User identifier of sticker file owner
  - **sticker**: InputFile (Required: True)
    - A file with the sticker in .WEBP, .PNG, .TGS, or .WEBM format. See https://core.telegram.org/stickers for technical requirements. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
  - **sticker_format**: String (Required: True)
    - Format of the sticker, must be one of "static", "animated", "video"
- **Returns**: File

---

### ⚙️ createNewStickerSet <a id='createnewstickerset'></a>
- **URL**: [https://core.telegram.org/bots/api#createnewstickerset](https://core.telegram.org/bots/api#createnewstickerset)
- **Description**:
  - Use this method to create a new sticker set owned by a user. The bot will be able to edit the sticker set thus created. Returns True on success.
- **Fields**:
  - **user_id**: Integer (Required: True)
    - User identifier of created sticker set owner
  - **name**: String (Required: True)
    - Short name of sticker set, to be used in t.me/addstickers/ URLs (e.g., animals). Can contain only English letters, digits and underscores. Must begin with a letter, can't contain consecutive underscores and must end in "_by_<bot_username>". <bot_username> is case insensitive. 1-64 characters.
  - **title**: String (Required: True)
    - Sticker set title, 1-64 characters
  - **stickers**: Array of InputSticker (Required: True)
    - A JSON-serialized list of 1-50 initial stickers to be added to the sticker set
  - **sticker_type**: String (Required: False)
    - Type of stickers in the set, pass "regular", "mask", or "custom_emoji". By default, a regular sticker set is created.
  - **needs_repainting**: Boolean (Required: False)
    - Pass True if stickers in the sticker set must be repainted to the color of text when used in messages, the accent color if used as emoji status, white on chat photos, or another appropriate color based on context; for custom emoji sticker sets only
- **Returns**: Boolean

---

### ⚙️ addStickerToSet <a id='addstickertoset'></a>
- **URL**: [https://core.telegram.org/bots/api#addstickertoset](https://core.telegram.org/bots/api#addstickertoset)
- **Description**:
  - Use this method to add a new sticker to a set created by the bot. Emoji sticker sets can have up to 200 stickers. Other sticker sets can have up to 120 stickers. Returns True on success.
- **Fields**:
  - **user_id**: Integer (Required: True)
    - User identifier of sticker set owner
  - **name**: String (Required: True)
    - Sticker set name
  - **sticker**: InputSticker (Required: True)
    - A JSON-serialized object with information about the added sticker. If exactly the same sticker had already been added to the set, then the set isn't changed.
- **Returns**: Boolean

---

### ⚙️ setStickerPositionInSet <a id='setstickerpositioninset'></a>
- **URL**: [https://core.telegram.org/bots/api#setstickerpositioninset](https://core.telegram.org/bots/api#setstickerpositioninset)
- **Description**:
  - Use this method to move a sticker in a set created by the bot to a specific position. Returns True on success.
- **Fields**:
  - **sticker**: String (Required: True)
    - File identifier of the sticker
  - **position**: Integer (Required: True)
    - New sticker position in the set, zero-based
- **Returns**: Boolean

---

### ⚙️ deleteStickerFromSet <a id='deletestickerfromset'></a>
- **URL**: [https://core.telegram.org/bots/api#deletestickerfromset](https://core.telegram.org/bots/api#deletestickerfromset)
- **Description**:
  - Use this method to delete a sticker from a set created by the bot. Returns True on success.
- **Fields**:
  - **sticker**: String (Required: True)
    - File identifier of the sticker
- **Returns**: Boolean

---

### ⚙️ replaceStickerInSet <a id='replacestickerinset'></a>
- **URL**: [https://core.telegram.org/bots/api#replacestickerinset](https://core.telegram.org/bots/api#replacestickerinset)
- **Description**:
  - Use this method to replace an existing sticker in a sticker set with a new one. The method is equivalent to calling deleteStickerFromSet, then addStickerToSet, then setStickerPositionInSet. Returns True on success.
- **Fields**:
  - **user_id**: Integer (Required: True)
    - User identifier of the sticker set owner
  - **name**: String (Required: True)
    - Sticker set name
  - **old_sticker**: String (Required: True)
    - File identifier of the replaced sticker
  - **sticker**: InputSticker (Required: True)
    - A JSON-serialized object with information about the added sticker. If exactly the same sticker had already been added to the set, then the set remains unchanged.
- **Returns**: Boolean

---

### ⚙️ setStickerEmojiList <a id='setstickeremojilist'></a>
- **URL**: [https://core.telegram.org/bots/api#setstickeremojilist](https://core.telegram.org/bots/api#setstickeremojilist)
- **Description**:
  - Use this method to change the list of emoji assigned to a regular or custom emoji sticker. The sticker must belong to a sticker set created by the bot. Returns True on success.
- **Fields**:
  - **sticker**: String (Required: True)
    - File identifier of the sticker
  - **emoji_list**: Array of String (Required: True)
    - A JSON-serialized list of 1-20 emoji associated with the sticker
- **Returns**: Boolean

---

### ⚙️ setStickerKeywords <a id='setstickerkeywords'></a>
- **URL**: [https://core.telegram.org/bots/api#setstickerkeywords](https://core.telegram.org/bots/api#setstickerkeywords)
- **Description**:
  - Use this method to change search keywords assigned to a regular or custom emoji sticker. The sticker must belong to a sticker set created by the bot. Returns True on success.
- **Fields**:
  - **sticker**: String (Required: True)
    - File identifier of the sticker
  - **keywords**: Array of String (Required: False)
    - A JSON-serialized list of 0-20 search keywords for the sticker with total length of up to 64 characters
- **Returns**: Boolean

---

### ⚙️ setStickerMaskPosition <a id='setstickermaskposition'></a>
- **URL**: [https://core.telegram.org/bots/api#setstickermaskposition](https://core.telegram.org/bots/api#setstickermaskposition)
- **Description**:
  - Use this method to change the mask position of a mask sticker. The sticker must belong to a sticker set that was created by the bot. Returns True on success.
- **Fields**:
  - **sticker**: String (Required: True)
    - File identifier of the sticker
  - **mask_position**: MaskPosition (Required: False)
    - A JSON-serialized object with the position where the mask should be placed on faces. Omit the parameter to remove the mask position.
- **Returns**: Boolean

---

### ⚙️ setStickerSetTitle <a id='setstickersettitle'></a>
- **URL**: [https://core.telegram.org/bots/api#setstickersettitle](https://core.telegram.org/bots/api#setstickersettitle)
- **Description**:
  - Use this method to set the title of a created sticker set. Returns True on success.
- **Fields**:
  - **name**: String (Required: True)
    - Sticker set name
  - **title**: String (Required: True)
    - Sticker set title, 1-64 characters
- **Returns**: Boolean

---

### ⚙️ setStickerSetThumbnail <a id='setstickersetthumbnail'></a>
- **URL**: [https://core.telegram.org/bots/api#setstickersetthumbnail](https://core.telegram.org/bots/api#setstickersetthumbnail)
- **Description**:
  - Use this method to set the thumbnail of a regular or mask sticker set. The format of the thumbnail file must match the format of the stickers in the set. Returns True on success.
- **Fields**:
  - **name**: String (Required: True)
    - Sticker set name
  - **user_id**: Integer (Required: True)
    - User identifier of the sticker set owner
  - **thumbnail**: InputFile, String (Required: False)
    - A .WEBP or .PNG image with the thumbnail, must be up to 128 kilobytes in size and have a width and height of exactly 100px, or a .TGS animation with a thumbnail up to 32 kilobytes in size (see https://core.telegram.org/stickers#animation-requirements for animated sticker technical requirements), or a WEBM video with the thumbnail up to 32 kilobytes in size; see https://core.telegram.org/stickers#video-requirements for video sticker technical requirements. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More information on Sending Files: https://core.telegram.org/bots/api#sending-files. Animated and video sticker set thumbnails can't be uploaded via HTTP URL. If omitted, then the thumbnail is dropped and the first sticker is used as the thumbnail.
  - **format**: String (Required: True)
    - Format of the thumbnail, must be one of "static" for a .WEBP or .PNG image, "animated" for a .TGS animation, or "video" for a WEBM video
- **Returns**: Boolean

---

### ⚙️ setCustomEmojiStickerSetThumbnail <a id='setcustomemojistickersetthumbnail'></a>
- **URL**: [https://core.telegram.org/bots/api#setcustomemojistickersetthumbnail](https://core.telegram.org/bots/api#setcustomemojistickersetthumbnail)
- **Description**:
  - Use this method to set the thumbnail of a custom emoji sticker set. Returns True on success.
- **Fields**:
  - **name**: String (Required: True)
    - Sticker set name
  - **custom_emoji_id**: String (Required: False)
    - Custom emoji identifier of a sticker from the sticker set; pass an empty string to drop the thumbnail and use the first sticker as the thumbnail.
- **Returns**: Boolean

---

### ⚙️ deleteStickerSet <a id='deletestickerset'></a>
- **URL**: [https://core.telegram.org/bots/api#deletestickerset](https://core.telegram.org/bots/api#deletestickerset)
- **Description**:
  - Use this method to delete a sticker set that was created by the bot. Returns True on success.
- **Fields**:
  - **name**: String (Required: True)
    - Sticker set name
- **Returns**: Boolean

---

### ⚙️ answerInlineQuery <a id='answerinlinequery'></a>
- **URL**: [https://core.telegram.org/bots/api#answerinlinequery](https://core.telegram.org/bots/api#answerinlinequery)
- **Description**:
  - Use this method to send answers to an inline query. On success, True is returned.
  - No more than 50 results per query are allowed.
- **Fields**:
  - **inline_query_id**: String (Required: True)
    - Unique identifier for the answered query
  - **results**: Array of InlineQueryResult (Required: True)
    - A JSON-serialized array of results for the inline query
  - **cache_time**: Integer (Required: False)
    - The maximum amount of time in seconds that the result of the inline query may be cached on the server. Defaults to 300.
  - **is_personal**: Boolean (Required: False)
    - Pass True if results may be cached on the server side only for the user that sent the query. By default, results may be returned to any user who sends the same query.
  - **next_offset**: String (Required: False)
    - Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don't support pagination. Offset length can't exceed 64 bytes.
  - **button**: InlineQueryResultsButton (Required: False)
    - A JSON-serialized object describing a button to be shown above inline query results
- **Returns**: Boolean

---

### ⚙️ answerWebAppQuery <a id='answerwebappquery'></a>
- **URL**: [https://core.telegram.org/bots/api#answerwebappquery](https://core.telegram.org/bots/api#answerwebappquery)
- **Description**:
  - Use this method to set the result of an interaction with a Web App and send a corresponding message on behalf of the user to the chat from which the query originated. On success, a SentWebAppMessage object is returned.
- **Fields**:
  - **web_app_query_id**: String (Required: True)
    - Unique identifier for the query to be answered
  - **result**: InlineQueryResult (Required: True)
    - A JSON-serialized object describing the message to be sent
- **Returns**: SentWebAppMessage

---

### ⚙️ sendInvoice <a id='sendinvoice'></a>
- **URL**: [https://core.telegram.org/bots/api#sendinvoice](https://core.telegram.org/bots/api#sendinvoice)
- **Description**:
  - Use this method to send invoices. On success, the sent Message is returned.
- **Fields**:
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target channel (in the format @channelusername)
  - **message_thread_id**: Integer (Required: False)
    - Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
  - **title**: String (Required: True)
    - Product name, 1-32 characters
  - **description**: String (Required: True)
    - Product description, 1-255 characters
  - **payload**: String (Required: True)
    - Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use it for your internal processes.
  - **provider_token**: String (Required: False)
    - Payment provider token, obtained via @BotFather. Pass an empty string for payments in Telegram Stars.
  - **currency**: String (Required: True)
    - Three-letter ISO 4217 currency code, see more on currencies. Pass "XTR" for payments in Telegram Stars.
  - **prices**: Array of LabeledPrice (Required: True)
    - Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in Telegram Stars.
  - **max_tip_amount**: Integer (Required: False)
    - The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0. Not supported for payments in Telegram Stars.
  - **suggested_tip_amounts**: Array of Integer (Required: False)
    - A JSON-serialized array of suggested amounts of tips in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.
  - **start_parameter**: String (Required: False)
    - Unique deep-linking parameter. If left empty, forwarded copies of the sent message will have a Pay button, allowing multiple users to pay directly from the forwarded message, using the same invoice. If non-empty, forwarded copies of the sent message will have a URL button with a deep link to the bot (instead of a Pay button), with the value used as the start parameter
  - **provider_data**: String (Required: False)
    - JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider.
  - **photo_url**: String (Required: False)
    - URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for.
  - **photo_size**: Integer (Required: False)
    - Photo size in bytes
  - **photo_width**: Integer (Required: False)
    - Photo width
  - **photo_height**: Integer (Required: False)
    - Photo height
  - **need_name**: Boolean (Required: False)
    - Pass True if you require the user's full name to complete the order. Ignored for payments in Telegram Stars.
  - **need_phone_number**: Boolean (Required: False)
    - Pass True if you require the user's phone number to complete the order. Ignored for payments in Telegram Stars.
  - **need_email**: Boolean (Required: False)
    - Pass True if you require the user's email address to complete the order. Ignored for payments in Telegram Stars.
  - **need_shipping_address**: Boolean (Required: False)
    - Pass True if you require the user's shipping address to complete the order. Ignored for payments in Telegram Stars.
  - **send_phone_number_to_provider**: Boolean (Required: False)
    - Pass True if the user's phone number should be sent to the provider. Ignored for payments in Telegram Stars.
  - **send_email_to_provider**: Boolean (Required: False)
    - Pass True if the user's email address should be sent to the provider. Ignored for payments in Telegram Stars.
  - **is_flexible**: Boolean (Required: False)
    - Pass True if the final price depends on the shipping method. Ignored for payments in Telegram Stars.
  - **disable_notification**: Boolean (Required: False)
    - Sends the message silently. Users will receive a notification with no sound.
  - **protect_content**: Boolean (Required: False)
    - Protects the contents of the sent message from forwarding and saving
  - **message_effect_id**: String (Required: False)
    - Unique identifier of the message effect to be added to the message; for private chats only
  - **reply_parameters**: ReplyParameters (Required: False)
    - Description of the message to reply to
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - A JSON-serialized object for an inline keyboard. If empty, one 'Pay total price' button will be shown. If not empty, the first button must be a Pay button.
- **Returns**: Message

---

### ⚙️ createInvoiceLink <a id='createinvoicelink'></a>
- **URL**: [https://core.telegram.org/bots/api#createinvoicelink](https://core.telegram.org/bots/api#createinvoicelink)
- **Description**:
  - Use this method to create a link for an invoice. Returns the created invoice link as String on success.
- **Fields**:
  - **title**: String (Required: True)
    - Product name, 1-32 characters
  - **description**: String (Required: True)
    - Product description, 1-255 characters
  - **payload**: String (Required: True)
    - Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use it for your internal processes.
  - **provider_token**: String (Required: False)
    - Payment provider token, obtained via @BotFather. Pass an empty string for payments in Telegram Stars.
  - **currency**: String (Required: True)
    - Three-letter ISO 4217 currency code, see more on currencies. Pass "XTR" for payments in Telegram Stars.
  - **prices**: Array of LabeledPrice (Required: True)
    - Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in Telegram Stars.
  - **max_tip_amount**: Integer (Required: False)
    - The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0. Not supported for payments in Telegram Stars.
  - **suggested_tip_amounts**: Array of Integer (Required: False)
    - A JSON-serialized array of suggested amounts of tips in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.
  - **provider_data**: String (Required: False)
    - JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider.
  - **photo_url**: String (Required: False)
    - URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service.
  - **photo_size**: Integer (Required: False)
    - Photo size in bytes
  - **photo_width**: Integer (Required: False)
    - Photo width
  - **photo_height**: Integer (Required: False)
    - Photo height
  - **need_name**: Boolean (Required: False)
    - Pass True if you require the user's full name to complete the order. Ignored for payments in Telegram Stars.
  - **need_phone_number**: Boolean (Required: False)
    - Pass True if you require the user's phone number to complete the order. Ignored for payments in Telegram Stars.
  - **need_email**: Boolean (Required: False)
    - Pass True if you require the user's email address to complete the order. Ignored for payments in Telegram Stars.
  - **need_shipping_address**: Boolean (Required: False)
    - Pass True if you require the user's shipping address to complete the order. Ignored for payments in Telegram Stars.
  - **send_phone_number_to_provider**: Boolean (Required: False)
    - Pass True if the user's phone number should be sent to the provider. Ignored for payments in Telegram Stars.
  - **send_email_to_provider**: Boolean (Required: False)
    - Pass True if the user's email address should be sent to the provider. Ignored for payments in Telegram Stars.
  - **is_flexible**: Boolean (Required: False)
    - Pass True if the final price depends on the shipping method. Ignored for payments in Telegram Stars.
- **Returns**: String

---

### ⚙️ answerShippingQuery <a id='answershippingquery'></a>
- **URL**: [https://core.telegram.org/bots/api#answershippingquery](https://core.telegram.org/bots/api#answershippingquery)
- **Description**:
  - If you sent an invoice requesting a shipping address and the parameter is_flexible was specified, the Bot API will send an Update with a shipping_query field to the bot. Use this method to reply to shipping queries. On success, True is returned.
- **Fields**:
  - **shipping_query_id**: String (Required: True)
    - Unique identifier for the query to be answered
  - **ok**: Boolean (Required: True)
    - Pass True if delivery to the specified address is possible and False if there are any problems (for example, if delivery to the specified address is not possible)
  - **shipping_options**: Array of ShippingOption (Required: False)
    - Required if ok is True. A JSON-serialized array of available shipping options.
  - **error_message**: String (Required: False)
    - Required if ok is False. Error message in human readable form that explains why it is impossible to complete the order (e.g. "Sorry, delivery to your desired address is unavailable'). Telegram will display this message to the user.
- **Returns**: Boolean

---

### ⚙️ answerPreCheckoutQuery <a id='answerprecheckoutquery'></a>
- **URL**: [https://core.telegram.org/bots/api#answerprecheckoutquery](https://core.telegram.org/bots/api#answerprecheckoutquery)
- **Description**:
  - Once the user has confirmed their payment and shipping details, the Bot API sends the final confirmation in the form of an Update with the field pre_checkout_query. Use this method to respond to such pre-checkout queries. On success, True is returned. Note: The Bot API must receive an answer within 10 seconds after the pre-checkout query was sent.
- **Fields**:
  - **pre_checkout_query_id**: String (Required: True)
    - Unique identifier for the query to be answered
  - **ok**: Boolean (Required: True)
    - Specify True if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order. Use False if there are any problems.
  - **error_message**: String (Required: False)
    - Required if ok is False. Error message in human readable form that explains the reason for failure to proceed with the checkout (e.g. "Sorry, somebody just bought the last of our amazing black T-shirts while you were busy filling out your payment details. Please choose a different color or garment!"). Telegram will display this message to the user.
- **Returns**: Boolean

---

### ⚙️ getStarTransactions <a id='getstartransactions'></a>
- **URL**: [https://core.telegram.org/bots/api#getstartransactions](https://core.telegram.org/bots/api#getstartransactions)
- **Description**:
  - Returns the bot's Telegram Star transactions in chronological order. On success, returns a StarTransactions object.
- **Fields**:
  - **offset**: Integer (Required: False)
    - Number of transactions to skip in the response
  - **limit**: Integer (Required: False)
    - The maximum number of transactions to be retrieved. Values between 1-100 are accepted. Defaults to 100.
- **Returns**: StarTransactions

---

### ⚙️ refundStarPayment <a id='refundstarpayment'></a>
- **URL**: [https://core.telegram.org/bots/api#refundstarpayment](https://core.telegram.org/bots/api#refundstarpayment)
- **Description**:
  - Refunds a successful payment in Telegram Stars. Returns True on success.
- **Fields**:
  - **user_id**: Integer (Required: True)
    - Identifier of the user whose payment will be refunded
  - **telegram_payment_charge_id**: String (Required: True)
    - Telegram payment identifier
- **Returns**: Boolean

---

### ⚙️ setPassportDataErrors <a id='setpassportdataerrors'></a>
- **URL**: [https://core.telegram.org/bots/api#setpassportdataerrors](https://core.telegram.org/bots/api#setpassportdataerrors)
- **Description**:
  - Informs a user that some of the Telegram Passport elements they provided contains errors. The user will not be able to re-submit their Passport to you until the errors are fixed (the contents of the field for which you returned the error must change). Returns True on success.
  - Use this if the data submitted by the user doesn't satisfy the standards your service requires for any reason. For example, if a birthday date seems invalid, a submitted document is blurry, a scan shows evidence of tampering, etc. Supply some details in the error message to make sure the user knows how to correct the issues.
- **Fields**:
  - **user_id**: Integer (Required: True)
    - User identifier
  - **errors**: Array of PassportElementError (Required: True)
    - A JSON-serialized array describing the errors
- **Returns**: Boolean

---

### ⚙️ sendGame <a id='sendgame'></a>
- **URL**: [https://core.telegram.org/bots/api#sendgame](https://core.telegram.org/bots/api#sendgame)
- **Description**:
  - Use this method to send a game. On success, the sent Message is returned.
- **Fields**:
  - **business_connection_id**: String (Required: False)
    - Unique identifier of the business connection on behalf of which the message will be sent
  - **chat_id**: Integer (Required: True)
    - Unique identifier for the target chat
  - **message_thread_id**: Integer (Required: False)
    - Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
  - **game_short_name**: String (Required: True)
    - Short name of the game, serves as the unique identifier for the game. Set up your games via @BotFather.
  - **disable_notification**: Boolean (Required: False)
    - Sends the message silently. Users will receive a notification with no sound.
  - **protect_content**: Boolean (Required: False)
    - Protects the contents of the sent message from forwarding and saving
  - **message_effect_id**: String (Required: False)
    - Unique identifier of the message effect to be added to the message; for private chats only
  - **reply_parameters**: ReplyParameters (Required: False)
    - Description of the message to reply to
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - A JSON-serialized object for an inline keyboard. If empty, one 'Play game_title' button will be shown. If not empty, the first button must launch the game.
- **Returns**: Message

---

### ⚙️ setGameScore <a id='setgamescore'></a>
- **URL**: [https://core.telegram.org/bots/api#setgamescore](https://core.telegram.org/bots/api#setgamescore)
- **Description**:
  - Use this method to set the score of the specified user in a game message. On success, if the message is not an inline message, the Message is returned, otherwise True is returned. Returns an error, if the new score is not greater than the user's current score in the chat and force is False.
- **Fields**:
  - **user_id**: Integer (Required: True)
    - User identifier
  - **score**: Integer (Required: True)
    - New score, must be non-negative
  - **force**: Boolean (Required: False)
    - Pass True if the high score is allowed to decrease. This can be useful when fixing mistakes or banning cheaters
  - **disable_edit_message**: Boolean (Required: False)
    - Pass True if the game message should not be automatically edited to include the current scoreboard
  - **chat_id**: Integer (Required: False)
    - Required if inline_message_id is not specified. Unique identifier for the target chat
  - **message_id**: Integer (Required: False)
    - Required if inline_message_id is not specified. Identifier of the sent message
  - **inline_message_id**: String (Required: False)
    - Required if chat_id and message_id are not specified. Identifier of the inline message
- **Returns**: Message, Boolean

---

### ⚙️ getGameHighScores <a id='getgamehighscores'></a>
- **URL**: [https://core.telegram.org/bots/api#getgamehighscores](https://core.telegram.org/bots/api#getgamehighscores)
- **Description**:
  - Use this method to get data for high score tables. Will return the score of the specified user and several of their neighbors in a game. Returns an Array of GameHighScore objects.
- **Fields**:
  - **user_id**: Integer (Required: True)
    - Target user id
  - **chat_id**: Integer (Required: False)
    - Required if inline_message_id is not specified. Unique identifier for the target chat
  - **message_id**: Integer (Required: False)
    - Required if inline_message_id is not specified. Identifier of the sent message
  - **inline_message_id**: String (Required: False)
    - Required if chat_id and message_id are not specified. Identifier of the inline message
- **Returns**: Array of GameHighScore

---

## 🛠️ Types
### 📦 Update <a id='update'></a>
- **URL**: [https://core.telegram.org/bots/api#update](https://core.telegram.org/bots/api#update)
- **Description**:
  - This object represents an incoming update.
  - At most one of the optional parameters can be present in any given update.
- **Fields**:
  - **update_id**: Integer (Required: True)
    - The update's unique identifier. Update identifiers start from a certain positive number and increase sequentially. This identifier becomes especially handy if you're using webhooks, since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially.
  - **message**: Message (Required: False)
    - Optional. New incoming message of any kind - text, photo, sticker, etc.
  - **edited_message**: Message (Required: False)
    - Optional. New version of a message that is known to the bot and was edited. This update may at times be triggered by changes to message fields that are either unavailable or not actively used by your bot.
  - **channel_post**: Message (Required: False)
    - Optional. New incoming channel post of any kind - text, photo, sticker, etc.
  - **edited_channel_post**: Message (Required: False)
    - Optional. New version of a channel post that is known to the bot and was edited. This update may at times be triggered by changes to message fields that are either unavailable or not actively used by your bot.
  - **business_connection**: BusinessConnection (Required: False)
    - Optional. The bot was connected to or disconnected from a business account, or a user edited an existing connection with the bot
  - **business_message**: Message (Required: False)
    - Optional. New message from a connected business account
  - **edited_business_message**: Message (Required: False)
    - Optional. New version of a message from a connected business account
  - **deleted_business_messages**: BusinessMessagesDeleted (Required: False)
    - Optional. Messages were deleted from a connected business account
  - **message_reaction**: MessageReactionUpdated (Required: False)
    - Optional. A reaction to a message was changed by a user. The bot must be an administrator in the chat and must explicitly specify "message_reaction" in the list of allowed_updates to receive these updates. The update isn't received for reactions set by bots.
  - **message_reaction_count**: MessageReactionCountUpdated (Required: False)
    - Optional. Reactions to a message with anonymous reactions were changed. The bot must be an administrator in the chat and must explicitly specify "message_reaction_count" in the list of allowed_updates to receive these updates. The updates are grouped and can be sent with delay up to a few minutes.
  - **inline_query**: InlineQuery (Required: False)
    - Optional. New incoming inline query
  - **chosen_inline_result**: ChosenInlineResult (Required: False)
    - Optional. The result of an inline query that was chosen by a user and sent to their chat partner. Please see our documentation on the feedback collecting for details on how to enable these updates for your bot.
  - **callback_query**: CallbackQuery (Required: False)
    - Optional. New incoming callback query
  - **shipping_query**: ShippingQuery (Required: False)
    - Optional. New incoming shipping query. Only for invoices with flexible price
  - **pre_checkout_query**: PreCheckoutQuery (Required: False)
    - Optional. New incoming pre-checkout query. Contains full information about checkout
  - **purchased_paid_media**: PaidMediaPurchased (Required: False)
    - Optional. A user purchased paid media with a non-empty payload sent by the bot in a non-channel chat
  - **poll**: Poll (Required: False)
    - Optional. New poll state. Bots receive only updates about manually stopped polls and polls, which are sent by the bot
  - **poll_answer**: PollAnswer (Required: False)
    - Optional. A user changed their answer in a non-anonymous poll. Bots receive new votes only in polls that were sent by the bot itself.
  - **my_chat_member**: ChatMemberUpdated (Required: False)
    - Optional. The bot's chat member status was updated in a chat. For private chats, this update is received only when the bot is blocked or unblocked by the user.
  - **chat_member**: ChatMemberUpdated (Required: False)
    - Optional. A chat member's status was updated in a chat. The bot must be an administrator in the chat and must explicitly specify "chat_member" in the list of allowed_updates to receive these updates.
  - **chat_join_request**: ChatJoinRequest (Required: False)
    - Optional. A request to join the chat has been sent. The bot must have the can_invite_users administrator right in the chat to receive these updates.
  - **chat_boost**: ChatBoostUpdated (Required: False)
    - Optional. A chat boost was added or changed. The bot must be an administrator in the chat to receive these updates.
  - **removed_chat_boost**: ChatBoostRemoved (Required: False)
    - Optional. A boost was removed from a chat. The bot must be an administrator in the chat to receive these updates.

💡 --- 💡

### 📦 WebhookInfo <a id='webhookinfo'></a>
- **URL**: [https://core.telegram.org/bots/api#webhookinfo](https://core.telegram.org/bots/api#webhookinfo)
- **Description**:
  - Describes the current status of a webhook.
- **Fields**:
  - **url**: String (Required: True)
    - Webhook URL, may be empty if webhook is not set up
  - **has_custom_certificate**: Boolean (Required: True)
    - True, if a custom certificate was provided for webhook certificate checks
  - **pending_update_count**: Integer (Required: True)
    - Number of updates awaiting delivery
  - **ip_address**: String (Required: False)
    - Optional. Currently used webhook IP address
  - **last_error_date**: Integer (Required: False)
    - Optional. Unix time for the most recent error that happened when trying to deliver an update via webhook
  - **last_error_message**: String (Required: False)
    - Optional. Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook
  - **last_synchronization_error_date**: Integer (Required: False)
    - Optional. Unix time of the most recent error that happened when trying to synchronize available updates with Telegram datacenters
  - **max_connections**: Integer (Required: False)
    - Optional. The maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery
  - **allowed_updates**: Array of String (Required: False)
    - Optional. A list of update types the bot is subscribed to. Defaults to all update types except chat_member

💡 --- 💡

### 📦 User <a id='user'></a>
- **URL**: [https://core.telegram.org/bots/api#user](https://core.telegram.org/bots/api#user)
- **Description**:
  - This object represents a Telegram user or bot.
- **Fields**:
  - **id**: Integer (Required: True)
    - Unique identifier for this user or bot. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
  - **is_bot**: Boolean (Required: True)
    - True, if this user is a bot
  - **first_name**: String (Required: True)
    - User's or bot's first name
  - **last_name**: String (Required: False)
    - Optional. User's or bot's last name
  - **username**: String (Required: False)
    - Optional. User's or bot's username
  - **language_code**: String (Required: False)
    - Optional. IETF language tag of the user's language
  - **is_premium**: Boolean (Required: False)
    - Optional. True, if this user is a Telegram Premium user
  - **added_to_attachment_menu**: Boolean (Required: False)
    - Optional. True, if this user added the bot to the attachment menu
  - **can_join_groups**: Boolean (Required: False)
    - Optional. True, if the bot can be invited to groups. Returned only in getMe.
  - **can_read_all_group_messages**: Boolean (Required: False)
    - Optional. True, if privacy mode is disabled for the bot. Returned only in getMe.
  - **supports_inline_queries**: Boolean (Required: False)
    - Optional. True, if the bot supports inline queries. Returned only in getMe.
  - **can_connect_to_business**: Boolean (Required: False)
    - Optional. True, if the bot can be connected to a Telegram Business account to receive its messages. Returned only in getMe.
  - **has_main_web_app**: Boolean (Required: False)
    - Optional. True, if the bot has a main Web App. Returned only in getMe.

💡 --- 💡

### 📦 Chat <a id='chat'></a>
- **URL**: [https://core.telegram.org/bots/api#chat](https://core.telegram.org/bots/api#chat)
- **Description**:
  - This object represents a chat.
- **Fields**:
  - **id**: Integer (Required: True)
    - Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
  - **type**: String (Required: True)
    - Type of the chat, can be either "private", "group", "supergroup" or "channel"
  - **title**: String (Required: False)
    - Optional. Title, for supergroups, channels and group chats
  - **username**: String (Required: False)
    - Optional. Username, for private chats, supergroups and channels if available
  - **first_name**: String (Required: False)
    - Optional. First name of the other party in a private chat
  - **last_name**: String (Required: False)
    - Optional. Last name of the other party in a private chat
  - **is_forum**: Boolean (Required: False)
    - Optional. True, if the supergroup chat is a forum (has topics enabled)

💡 --- 💡

### 📦 ChatFullInfo <a id='chatfullinfo'></a>
- **URL**: [https://core.telegram.org/bots/api#chatfullinfo](https://core.telegram.org/bots/api#chatfullinfo)
- **Description**:
  - This object contains full information about a chat.
- **Fields**:
  - **id**: Integer (Required: True)
    - Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
  - **type**: String (Required: True)
    - Type of the chat, can be either "private", "group", "supergroup" or "channel"
  - **title**: String (Required: False)
    - Optional. Title, for supergroups, channels and group chats
  - **username**: String (Required: False)
    - Optional. Username, for private chats, supergroups and channels if available
  - **first_name**: String (Required: False)
    - Optional. First name of the other party in a private chat
  - **last_name**: String (Required: False)
    - Optional. Last name of the other party in a private chat
  - **is_forum**: Boolean (Required: False)
    - Optional. True, if the supergroup chat is a forum (has topics enabled)
  - **accent_color_id**: Integer (Required: True)
    - Identifier of the accent color for the chat name and backgrounds of the chat photo, reply header, and link preview. See accent colors for more details.
  - **max_reaction_count**: Integer (Required: True)
    - The maximum number of reactions that can be set on a message in the chat
  - **photo**: ChatPhoto (Required: False)
    - Optional. Chat photo
  - **active_usernames**: Array of String (Required: False)
    - Optional. If non-empty, the list of all active chat usernames; for private chats, supergroups and channels
  - **birthdate**: Birthdate (Required: False)
    - Optional. For private chats, the date of birth of the user
  - **business_intro**: BusinessIntro (Required: False)
    - Optional. For private chats with business accounts, the intro of the business
  - **business_location**: BusinessLocation (Required: False)
    - Optional. For private chats with business accounts, the location of the business
  - **business_opening_hours**: BusinessOpeningHours (Required: False)
    - Optional. For private chats with business accounts, the opening hours of the business
  - **personal_chat**: Chat (Required: False)
    - Optional. For private chats, the personal channel of the user
  - **available_reactions**: Array of ReactionType (Required: False)
    - Optional. List of available reactions allowed in the chat. If omitted, then all emoji reactions are allowed.
  - **background_custom_emoji_id**: String (Required: False)
    - Optional. Custom emoji identifier of the emoji chosen by the chat for the reply header and link preview background
  - **profile_accent_color_id**: Integer (Required: False)
    - Optional. Identifier of the accent color for the chat's profile background. See profile accent colors for more details.
  - **profile_background_custom_emoji_id**: String (Required: False)
    - Optional. Custom emoji identifier of the emoji chosen by the chat for its profile background
  - **emoji_status_custom_emoji_id**: String (Required: False)
    - Optional. Custom emoji identifier of the emoji status of the chat or the other party in a private chat
  - **emoji_status_expiration_date**: Integer (Required: False)
    - Optional. Expiration date of the emoji status of the chat or the other party in a private chat, in Unix time, if any
  - **bio**: String (Required: False)
    - Optional. Bio of the other party in a private chat
  - **has_private_forwards**: Boolean (Required: False)
    - Optional. True, if privacy settings of the other party in the private chat allows to use tg://user?id=<user_id> links only in chats with the user
  - **has_restricted_voice_and_video_messages**: Boolean (Required: False)
    - Optional. True, if the privacy settings of the other party restrict sending voice and video note messages in the private chat
  - **join_to_send_messages**: Boolean (Required: False)
    - Optional. True, if users need to join the supergroup before they can send messages
  - **join_by_request**: Boolean (Required: False)
    - Optional. True, if all users directly joining the supergroup without using an invite link need to be approved by supergroup administrators
  - **description**: String (Required: False)
    - Optional. Description, for groups, supergroups and channel chats
  - **invite_link**: String (Required: False)
    - Optional. Primary invite link, for groups, supergroups and channel chats
  - **pinned_message**: Message (Required: False)
    - Optional. The most recent pinned message (by sending date)
  - **permissions**: ChatPermissions (Required: False)
    - Optional. Default chat member permissions, for groups and supergroups
  - **can_send_paid_media**: Boolean (Required: False)
    - Optional. True, if paid media messages can be sent or forwarded to the channel chat. The field is available only for channel chats.
  - **slow_mode_delay**: Integer (Required: False)
    - Optional. For supergroups, the minimum allowed delay between consecutive messages sent by each unprivileged user; in seconds
  - **unrestrict_boost_count**: Integer (Required: False)
    - Optional. For supergroups, the minimum number of boosts that a non-administrator user needs to add in order to ignore slow mode and chat permissions
  - **message_auto_delete_time**: Integer (Required: False)
    - Optional. The time after which all messages sent to the chat will be automatically deleted; in seconds
  - **has_aggressive_anti_spam_enabled**: Boolean (Required: False)
    - Optional. True, if aggressive anti-spam checks are enabled in the supergroup. The field is only available to chat administrators.
  - **has_hidden_members**: Boolean (Required: False)
    - Optional. True, if non-administrators can only get the list of bots and administrators in the chat
  - **has_protected_content**: Boolean (Required: False)
    - Optional. True, if messages from the chat can't be forwarded to other chats
  - **has_visible_history**: Boolean (Required: False)
    - Optional. True, if new chat members will have access to old messages; available only to chat administrators
  - **sticker_set_name**: String (Required: False)
    - Optional. For supergroups, name of the group sticker set
  - **can_set_sticker_set**: Boolean (Required: False)
    - Optional. True, if the bot can change the group sticker set
  - **custom_emoji_sticker_set_name**: String (Required: False)
    - Optional. For supergroups, the name of the group's custom emoji sticker set. Custom emoji from this set can be used by all users and bots in the group.
  - **linked_chat_id**: Integer (Required: False)
    - Optional. Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
  - **location**: ChatLocation (Required: False)
    - Optional. For supergroups, the location to which the supergroup is connected

💡 --- 💡

### 📦 Message <a id='message'></a>
- **URL**: [https://core.telegram.org/bots/api#message](https://core.telegram.org/bots/api#message)
- **Description**:
  - This object represents a message.
- **Fields**:
  - **message_id**: Integer (Required: True)
    - Unique message identifier inside this chat
  - **message_thread_id**: Integer (Required: False)
    - Optional. Unique identifier of a message thread to which the message belongs; for supergroups only
  - **from**: User (Required: False)
    - Optional. Sender of the message; may be empty for messages sent to channels. For backward compatibility, if the message was sent on behalf of a chat, the field contains a fake sender user in non-channel chats
  - **sender_chat**: Chat (Required: False)
    - Optional. Sender of the message when sent on behalf of a chat. For example, the supergroup itself for messages sent by its anonymous administrators or a linked channel for messages automatically forwarded to the channel's discussion group. For backward compatibility, if the message was sent on behalf of a chat, the field from contains a fake sender user in non-channel chats.
  - **sender_boost_count**: Integer (Required: False)
    - Optional. If the sender of the message boosted the chat, the number of boosts added by the user
  - **sender_business_bot**: User (Required: False)
    - Optional. The bot that actually sent the message on behalf of the business account. Available only for outgoing messages sent on behalf of the connected business account.
  - **date**: Integer (Required: True)
    - Date the message was sent in Unix time. It is always a positive number, representing a valid date.
  - **business_connection_id**: String (Required: False)
    - Optional. Unique identifier of the business connection from which the message was received. If non-empty, the message belongs to a chat of the corresponding business account that is independent from any potential bot chat which might share the same identifier.
  - **chat**: Chat (Required: True)
    - Chat the message belongs to
  - **forward_origin**: MessageOrigin (Required: False)
    - Optional. Information about the original message for forwarded messages
  - **is_topic_message**: Boolean (Required: False)
    - Optional. True, if the message is sent to a forum topic
  - **is_automatic_forward**: Boolean (Required: False)
    - Optional. True, if the message is a channel post that was automatically forwarded to the connected discussion group
  - **reply_to_message**: Message (Required: False)
    - Optional. For replies in the same chat and message thread, the original message. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.
  - **external_reply**: ExternalReplyInfo (Required: False)
    - Optional. Information about the message that is being replied to, which may come from another chat or forum topic
  - **quote**: TextQuote (Required: False)
    - Optional. For replies that quote part of the original message, the quoted part of the message
  - **reply_to_story**: Story (Required: False)
    - Optional. For replies to a story, the original story
  - **via_bot**: User (Required: False)
    - Optional. Bot through which the message was sent
  - **edit_date**: Integer (Required: False)
    - Optional. Date the message was last edited in Unix time
  - **has_protected_content**: Boolean (Required: False)
    - Optional. True, if the message can't be forwarded
  - **is_from_offline**: Boolean (Required: False)
    - Optional. True, if the message was sent by an implicit action, for example, as an away or a greeting business message, or as a scheduled message
  - **media_group_id**: String (Required: False)
    - Optional. The unique identifier of a media message group this message belongs to
  - **author_signature**: String (Required: False)
    - Optional. Signature of the post author for messages in channels, or the custom title of an anonymous group administrator
  - **text**: String (Required: False)
    - Optional. For text messages, the actual UTF-8 text of the message
  - **entities**: Array of MessageEntity (Required: False)
    - Optional. For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text
  - **link_preview_options**: LinkPreviewOptions (Required: False)
    - Optional. Options used for link preview generation for the message, if it is a text message and link preview options were changed
  - **effect_id**: String (Required: False)
    - Optional. Unique identifier of the message effect added to the message
  - **animation**: Animation (Required: False)
    - Optional. Message is an animation, information about the animation. For backward compatibility, when this field is set, the document field will also be set
  - **audio**: Audio (Required: False)
    - Optional. Message is an audio file, information about the file
  - **document**: Document (Required: False)
    - Optional. Message is a general file, information about the file
  - **paid_media**: PaidMediaInfo (Required: False)
    - Optional. Message contains paid media; information about the paid media
  - **photo**: Array of PhotoSize (Required: False)
    - Optional. Message is a photo, available sizes of the photo
  - **sticker**: Sticker (Required: False)
    - Optional. Message is a sticker, information about the sticker
  - **story**: Story (Required: False)
    - Optional. Message is a forwarded story
  - **video**: Video (Required: False)
    - Optional. Message is a video, information about the video
  - **video_note**: VideoNote (Required: False)
    - Optional. Message is a video note, information about the video message
  - **voice**: Voice (Required: False)
    - Optional. Message is a voice message, information about the file
  - **caption**: String (Required: False)
    - Optional. Caption for the animation, audio, document, paid media, photo, video or voice
  - **caption_entities**: Array of MessageEntity (Required: False)
    - Optional. For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption
  - **show_caption_above_media**: Boolean (Required: False)
    - Optional. True, if the caption must be shown above the message media
  - **has_media_spoiler**: Boolean (Required: False)
    - Optional. True, if the message media is covered by a spoiler animation
  - **contact**: Contact (Required: False)
    - Optional. Message is a shared contact, information about the contact
  - **dice**: Dice (Required: False)
    - Optional. Message is a dice with random value
  - **game**: Game (Required: False)
    - Optional. Message is a game, information about the game. More about games: https://core.telegram.org/bots/api#games
  - **poll**: Poll (Required: False)
    - Optional. Message is a native poll, information about the poll
  - **venue**: Venue (Required: False)
    - Optional. Message is a venue, information about the venue. For backward compatibility, when this field is set, the location field will also be set
  - **location**: Location (Required: False)
    - Optional. Message is a shared location, information about the location
  - **new_chat_members**: Array of User (Required: False)
    - Optional. New members that were added to the group or supergroup and information about them (the bot itself may be one of these members)
  - **left_chat_member**: User (Required: False)
    - Optional. A member was removed from the group, information about them (this member may be the bot itself)
  - **new_chat_title**: String (Required: False)
    - Optional. A chat title was changed to this value
  - **new_chat_photo**: Array of PhotoSize (Required: False)
    - Optional. A chat photo was change to this value
  - **delete_chat_photo**: Boolean (Required: False)
    - Optional. Service message: the chat photo was deleted
  - **group_chat_created**: Boolean (Required: False)
    - Optional. Service message: the group has been created
  - **supergroup_chat_created**: Boolean (Required: False)
    - Optional. Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in reply_to_message if someone replies to a very first message in a directly created supergroup.
  - **channel_chat_created**: Boolean (Required: False)
    - Optional. Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in reply_to_message if someone replies to a very first message in a channel.
  - **message_auto_delete_timer_changed**: MessageAutoDeleteTimerChanged (Required: False)
    - Optional. Service message: auto-delete timer settings changed in the chat
  - **migrate_to_chat_id**: Integer (Required: False)
    - Optional. The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
  - **migrate_from_chat_id**: Integer (Required: False)
    - Optional. The supergroup has been migrated from a group with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
  - **pinned_message**: MaybeInaccessibleMessage (Required: False)
    - Optional. Specified message was pinned. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.
  - **invoice**: Invoice (Required: False)
    - Optional. Message is an invoice for a payment, information about the invoice. More about payments: https://core.telegram.org/bots/api#payments
  - **successful_payment**: SuccessfulPayment (Required: False)
    - Optional. Message is a service message about a successful payment, information about the payment. More about payments: https://core.telegram.org/bots/api#payments
  - **refunded_payment**: RefundedPayment (Required: False)
    - Optional. Message is a service message about a refunded payment, information about the payment. More about payments: https://core.telegram.org/bots/api#payments
  - **users_shared**: UsersShared (Required: False)
    - Optional. Service message: users were shared with the bot
  - **chat_shared**: ChatShared (Required: False)
    - Optional. Service message: a chat was shared with the bot
  - **connected_website**: String (Required: False)
    - Optional. The domain name of the website on which the user has logged in. More about Telegram Login: https://core.telegram.org/widgets/login
  - **write_access_allowed**: WriteAccessAllowed (Required: False)
    - Optional. Service message: the user allowed the bot to write messages after adding it to the attachment or side menu, launching a Web App from a link, or accepting an explicit request from a Web App sent by the method requestWriteAccess
  - **passport_data**: PassportData (Required: False)
    - Optional. Telegram Passport data
  - **proximity_alert_triggered**: ProximityAlertTriggered (Required: False)
    - Optional. Service message. A user in the chat triggered another user's proximity alert while sharing Live Location.
  - **boost_added**: ChatBoostAdded (Required: False)
    - Optional. Service message: user boosted the chat
  - **chat_background_set**: ChatBackground (Required: False)
    - Optional. Service message: chat background set
  - **forum_topic_created**: ForumTopicCreated (Required: False)
    - Optional. Service message: forum topic created
  - **forum_topic_edited**: ForumTopicEdited (Required: False)
    - Optional. Service message: forum topic edited
  - **forum_topic_closed**: ForumTopicClosed (Required: False)
    - Optional. Service message: forum topic closed
  - **forum_topic_reopened**: ForumTopicReopened (Required: False)
    - Optional. Service message: forum topic reopened
  - **general_forum_topic_hidden**: GeneralForumTopicHidden (Required: False)
    - Optional. Service message: the 'General' forum topic hidden
  - **general_forum_topic_unhidden**: GeneralForumTopicUnhidden (Required: False)
    - Optional. Service message: the 'General' forum topic unhidden
  - **giveaway_created**: GiveawayCreated (Required: False)
    - Optional. Service message: a scheduled giveaway was created
  - **giveaway**: Giveaway (Required: False)
    - Optional. The message is a scheduled giveaway message
  - **giveaway_winners**: GiveawayWinners (Required: False)
    - Optional. A giveaway with public winners was completed
  - **giveaway_completed**: GiveawayCompleted (Required: False)
    - Optional. Service message: a giveaway without public winners was completed
  - **video_chat_scheduled**: VideoChatScheduled (Required: False)
    - Optional. Service message: video chat scheduled
  - **video_chat_started**: VideoChatStarted (Required: False)
    - Optional. Service message: video chat started
  - **video_chat_ended**: VideoChatEnded (Required: False)
    - Optional. Service message: video chat ended
  - **video_chat_participants_invited**: VideoChatParticipantsInvited (Required: False)
    - Optional. Service message: new participants invited to a video chat
  - **web_app_data**: WebAppData (Required: False)
    - Optional. Service message: data sent by a Web App
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - Optional. Inline keyboard attached to the message. login_url buttons are represented as ordinary url buttons.

💡 --- 💡

### 📦 MessageId <a id='messageid'></a>
- **URL**: [https://core.telegram.org/bots/api#messageid](https://core.telegram.org/bots/api#messageid)
- **Description**:
  - This object represents a unique message identifier.
- **Fields**:
  - **message_id**: Integer (Required: True)
    - Unique message identifier

💡 --- 💡

### 📦 InaccessibleMessage <a id='inaccessiblemessage'></a>
- **URL**: [https://core.telegram.org/bots/api#inaccessiblemessage](https://core.telegram.org/bots/api#inaccessiblemessage)
- **Description**:
  - This object describes a message that was deleted or is otherwise inaccessible to the bot.
- **Fields**:
  - **chat**: Chat (Required: True)
    - Chat the message belonged to
  - **message_id**: Integer (Required: True)
    - Unique message identifier inside the chat
  - **date**: Integer (Required: True)
    - Always 0. The field can be used to differentiate regular and inaccessible messages.

💡 --- 💡

### 📦 MaybeInaccessibleMessage <a id='maybeinaccessiblemessage'></a>
- **URL**: [https://core.telegram.org/bots/api#maybeinaccessiblemessage](https://core.telegram.org/bots/api#maybeinaccessiblemessage)
- **Description**:
  - This object describes a message that can be inaccessible to the bot. It can be one of
  - - Message
  - - InaccessibleMessage
- **Subtypes**:
  - Message
  - InaccessibleMessage

💡 --- 💡

### 📦 MessageEntity <a id='messageentity'></a>
- **URL**: [https://core.telegram.org/bots/api#messageentity](https://core.telegram.org/bots/api#messageentity)
- **Description**:
  - This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the entity. Currently, can be "mention" (@username), "hashtag" (#hashtag), "cashtag" ($USD), "bot_command" (/start@jobs_bot), "url" (https://telegram.org), "email" (do-not-reply@telegram.org), "phone_number" (+1-212-555-0123), "bold" (bold text), "italic" (italic text), "underline" (underlined text), "strikethrough" (strikethrough text), "spoiler" (spoiler message), "blockquote" (block quotation), "expandable_blockquote" (collapsed-by-default block quotation), "code" (monowidth string), "pre" (monowidth block), "text_link" (for clickable text URLs), "text_mention" (for users without usernames), "custom_emoji" (for inline custom emoji stickers)
  - **offset**: Integer (Required: True)
    - Offset in UTF-16 code units to the start of the entity
  - **length**: Integer (Required: True)
    - Length of the entity in UTF-16 code units
  - **url**: String (Required: False)
    - Optional. For "text_link" only, URL that will be opened after user taps on the text
  - **user**: User (Required: False)
    - Optional. For "text_mention" only, the mentioned user
  - **language**: String (Required: False)
    - Optional. For "pre" only, the programming language of the entity text
  - **custom_emoji_id**: String (Required: False)
    - Optional. For "custom_emoji" only, unique identifier of the custom emoji. Use getCustomEmojiStickers to get full information about the sticker

💡 --- 💡

### 📦 TextQuote <a id='textquote'></a>
- **URL**: [https://core.telegram.org/bots/api#textquote](https://core.telegram.org/bots/api#textquote)
- **Description**:
  - This object contains information about the quoted part of a message that is replied to by the given message.
- **Fields**:
  - **text**: String (Required: True)
    - Text of the quoted part of a message that is replied to by the given message
  - **entities**: Array of MessageEntity (Required: False)
    - Optional. Special entities that appear in the quote. Currently, only bold, italic, underline, strikethrough, spoiler, and custom_emoji entities are kept in quotes.
  - **position**: Integer (Required: True)
    - Approximate quote position in the original message in UTF-16 code units as specified by the sender
  - **is_manual**: Boolean (Required: False)
    - Optional. True, if the quote was chosen manually by the message sender. Otherwise, the quote was added automatically by the server.

💡 --- 💡

### 📦 ExternalReplyInfo <a id='externalreplyinfo'></a>
- **URL**: [https://core.telegram.org/bots/api#externalreplyinfo](https://core.telegram.org/bots/api#externalreplyinfo)
- **Description**:
  - This object contains information about a message that is being replied to, which may come from another chat or forum topic.
- **Fields**:
  - **origin**: MessageOrigin (Required: True)
    - Origin of the message replied to by the given message
  - **chat**: Chat (Required: False)
    - Optional. Chat the original message belongs to. Available only if the chat is a supergroup or a channel.
  - **message_id**: Integer (Required: False)
    - Optional. Unique message identifier inside the original chat. Available only if the original chat is a supergroup or a channel.
  - **link_preview_options**: LinkPreviewOptions (Required: False)
    - Optional. Options used for link preview generation for the original message, if it is a text message
  - **animation**: Animation (Required: False)
    - Optional. Message is an animation, information about the animation
  - **audio**: Audio (Required: False)
    - Optional. Message is an audio file, information about the file
  - **document**: Document (Required: False)
    - Optional. Message is a general file, information about the file
  - **paid_media**: PaidMediaInfo (Required: False)
    - Optional. Message contains paid media; information about the paid media
  - **photo**: Array of PhotoSize (Required: False)
    - Optional. Message is a photo, available sizes of the photo
  - **sticker**: Sticker (Required: False)
    - Optional. Message is a sticker, information about the sticker
  - **story**: Story (Required: False)
    - Optional. Message is a forwarded story
  - **video**: Video (Required: False)
    - Optional. Message is a video, information about the video
  - **video_note**: VideoNote (Required: False)
    - Optional. Message is a video note, information about the video message
  - **voice**: Voice (Required: False)
    - Optional. Message is a voice message, information about the file
  - **has_media_spoiler**: Boolean (Required: False)
    - Optional. True, if the message media is covered by a spoiler animation
  - **contact**: Contact (Required: False)
    - Optional. Message is a shared contact, information about the contact
  - **dice**: Dice (Required: False)
    - Optional. Message is a dice with random value
  - **game**: Game (Required: False)
    - Optional. Message is a game, information about the game. More about games: https://core.telegram.org/bots/api#games
  - **giveaway**: Giveaway (Required: False)
    - Optional. Message is a scheduled giveaway, information about the giveaway
  - **giveaway_winners**: GiveawayWinners (Required: False)
    - Optional. A giveaway with public winners was completed
  - **invoice**: Invoice (Required: False)
    - Optional. Message is an invoice for a payment, information about the invoice. More about payments: https://core.telegram.org/bots/api#payments
  - **location**: Location (Required: False)
    - Optional. Message is a shared location, information about the location
  - **poll**: Poll (Required: False)
    - Optional. Message is a native poll, information about the poll
  - **venue**: Venue (Required: False)
    - Optional. Message is a venue, information about the venue

💡 --- 💡

### 📦 ReplyParameters <a id='replyparameters'></a>
- **URL**: [https://core.telegram.org/bots/api#replyparameters](https://core.telegram.org/bots/api#replyparameters)
- **Description**:
  - Describes reply parameters for the message that is being sent.
- **Fields**:
  - **message_id**: Integer (Required: True)
    - Identifier of the message that will be replied to in the current chat, or in the chat chat_id if it is specified
  - **chat_id**: Integer, String (Required: False)
    - Optional. If the message to be replied to is from a different chat, unique identifier for the chat or username of the channel (in the format @channelusername). Not supported for messages sent on behalf of a business account.
  - **allow_sending_without_reply**: Boolean (Required: False)
    - Optional. Pass True if the message should be sent even if the specified message to be replied to is not found. Always False for replies in another chat or forum topic. Always True for messages sent on behalf of a business account.
  - **quote**: String (Required: False)
    - Optional. Quoted part of the message to be replied to; 0-1024 characters after entities parsing. The quote must be an exact substring of the message to be replied to, including bold, italic, underline, strikethrough, spoiler, and custom_emoji entities. The message will fail to send if the quote isn't found in the original message.
  - **quote_parse_mode**: String (Required: False)
    - Optional. Mode for parsing entities in the quote. See formatting options for more details.
  - **quote_entities**: Array of MessageEntity (Required: False)
    - Optional. A JSON-serialized list of special entities that appear in the quote. It can be specified instead of quote_parse_mode.
  - **quote_position**: Integer (Required: False)
    - Optional. Position of the quote in the original message in UTF-16 code units

💡 --- 💡

### 📦 MessageOrigin <a id='messageorigin'></a>
- **URL**: [https://core.telegram.org/bots/api#messageorigin](https://core.telegram.org/bots/api#messageorigin)
- **Description**:
  - This object describes the origin of a message. It can be one of
  - - MessageOriginUser
  - - MessageOriginHiddenUser
  - - MessageOriginChat
  - - MessageOriginChannel
- **Subtypes**:
  - MessageOriginUser
  - MessageOriginHiddenUser
  - MessageOriginChat
  - MessageOriginChannel

💡 --- 💡

### 📦 MessageOriginUser <a id='messageoriginuser'></a>
- **URL**: [https://core.telegram.org/bots/api#messageoriginuser](https://core.telegram.org/bots/api#messageoriginuser)
- **Description**:
  - The message was originally sent by a known user.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the message origin, always "user"
  - **date**: Integer (Required: True)
    - Date the message was sent originally in Unix time
  - **sender_user**: User (Required: True)
    - User that sent the message originally

💡 --- 💡

### 📦 MessageOriginHiddenUser <a id='messageoriginhiddenuser'></a>
- **URL**: [https://core.telegram.org/bots/api#messageoriginhiddenuser](https://core.telegram.org/bots/api#messageoriginhiddenuser)
- **Description**:
  - The message was originally sent by an unknown user.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the message origin, always "hidden_user"
  - **date**: Integer (Required: True)
    - Date the message was sent originally in Unix time
  - **sender_user_name**: String (Required: True)
    - Name of the user that sent the message originally

💡 --- 💡

### 📦 MessageOriginChat <a id='messageoriginchat'></a>
- **URL**: [https://core.telegram.org/bots/api#messageoriginchat](https://core.telegram.org/bots/api#messageoriginchat)
- **Description**:
  - The message was originally sent on behalf of a chat to a group chat.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the message origin, always "chat"
  - **date**: Integer (Required: True)
    - Date the message was sent originally in Unix time
  - **sender_chat**: Chat (Required: True)
    - Chat that sent the message originally
  - **author_signature**: String (Required: False)
    - Optional. For messages originally sent by an anonymous chat administrator, original message author signature

💡 --- 💡

### 📦 MessageOriginChannel <a id='messageoriginchannel'></a>
- **URL**: [https://core.telegram.org/bots/api#messageoriginchannel](https://core.telegram.org/bots/api#messageoriginchannel)
- **Description**:
  - The message was originally sent to a channel chat.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the message origin, always "channel"
  - **date**: Integer (Required: True)
    - Date the message was sent originally in Unix time
  - **chat**: Chat (Required: True)
    - Channel chat to which the message was originally sent
  - **message_id**: Integer (Required: True)
    - Unique message identifier inside the chat
  - **author_signature**: String (Required: False)
    - Optional. Signature of the original post author

💡 --- 💡

### 📦 PhotoSize <a id='photosize'></a>
- **URL**: [https://core.telegram.org/bots/api#photosize](https://core.telegram.org/bots/api#photosize)
- **Description**:
  - This object represents one size of a photo or a file / sticker thumbnail.
- **Fields**:
  - **file_id**: String (Required: True)
    - Identifier for this file, which can be used to download or reuse the file
  - **file_unique_id**: String (Required: True)
    - Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
  - **width**: Integer (Required: True)
    - Photo width
  - **height**: Integer (Required: True)
    - Photo height
  - **file_size**: Integer (Required: False)
    - Optional. File size in bytes

💡 --- 💡

### 📦 Animation <a id='animation'></a>
- **URL**: [https://core.telegram.org/bots/api#animation](https://core.telegram.org/bots/api#animation)
- **Description**:
  - This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).
- **Fields**:
  - **file_id**: String (Required: True)
    - Identifier for this file, which can be used to download or reuse the file
  - **file_unique_id**: String (Required: True)
    - Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
  - **width**: Integer (Required: True)
    - Video width as defined by the sender
  - **height**: Integer (Required: True)
    - Video height as defined by the sender
  - **duration**: Integer (Required: True)
    - Duration of the video in seconds as defined by the sender
  - **thumbnail**: PhotoSize (Required: False)
    - Optional. Animation thumbnail as defined by the sender
  - **file_name**: String (Required: False)
    - Optional. Original animation filename as defined by the sender
  - **mime_type**: String (Required: False)
    - Optional. MIME type of the file as defined by the sender
  - **file_size**: Integer (Required: False)
    - Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.

💡 --- 💡

### 📦 Audio <a id='audio'></a>
- **URL**: [https://core.telegram.org/bots/api#audio](https://core.telegram.org/bots/api#audio)
- **Description**:
  - This object represents an audio file to be treated as music by the Telegram clients.
- **Fields**:
  - **file_id**: String (Required: True)
    - Identifier for this file, which can be used to download or reuse the file
  - **file_unique_id**: String (Required: True)
    - Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
  - **duration**: Integer (Required: True)
    - Duration of the audio in seconds as defined by the sender
  - **performer**: String (Required: False)
    - Optional. Performer of the audio as defined by the sender or by audio tags
  - **title**: String (Required: False)
    - Optional. Title of the audio as defined by the sender or by audio tags
  - **file_name**: String (Required: False)
    - Optional. Original filename as defined by the sender
  - **mime_type**: String (Required: False)
    - Optional. MIME type of the file as defined by the sender
  - **file_size**: Integer (Required: False)
    - Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
  - **thumbnail**: PhotoSize (Required: False)
    - Optional. Thumbnail of the album cover to which the music file belongs

💡 --- 💡

### 📦 Document <a id='document'></a>
- **URL**: [https://core.telegram.org/bots/api#document](https://core.telegram.org/bots/api#document)
- **Description**:
  - This object represents a general file (as opposed to photos, voice messages and audio files).
- **Fields**:
  - **file_id**: String (Required: True)
    - Identifier for this file, which can be used to download or reuse the file
  - **file_unique_id**: String (Required: True)
    - Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
  - **thumbnail**: PhotoSize (Required: False)
    - Optional. Document thumbnail as defined by the sender
  - **file_name**: String (Required: False)
    - Optional. Original filename as defined by the sender
  - **mime_type**: String (Required: False)
    - Optional. MIME type of the file as defined by the sender
  - **file_size**: Integer (Required: False)
    - Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.

💡 --- 💡

### 📦 Story <a id='story'></a>
- **URL**: [https://core.telegram.org/bots/api#story](https://core.telegram.org/bots/api#story)
- **Description**:
  - This object represents a story.
- **Fields**:
  - **chat**: Chat (Required: True)
    - Chat that posted the story
  - **id**: Integer (Required: True)
    - Unique identifier for the story in the chat

💡 --- 💡

### 📦 Video <a id='video'></a>
- **URL**: [https://core.telegram.org/bots/api#video](https://core.telegram.org/bots/api#video)
- **Description**:
  - This object represents a video file.
- **Fields**:
  - **file_id**: String (Required: True)
    - Identifier for this file, which can be used to download or reuse the file
  - **file_unique_id**: String (Required: True)
    - Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
  - **width**: Integer (Required: True)
    - Video width as defined by the sender
  - **height**: Integer (Required: True)
    - Video height as defined by the sender
  - **duration**: Integer (Required: True)
    - Duration of the video in seconds as defined by the sender
  - **thumbnail**: PhotoSize (Required: False)
    - Optional. Video thumbnail
  - **file_name**: String (Required: False)
    - Optional. Original filename as defined by the sender
  - **mime_type**: String (Required: False)
    - Optional. MIME type of the file as defined by the sender
  - **file_size**: Integer (Required: False)
    - Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.

💡 --- 💡

### 📦 VideoNote <a id='videonote'></a>
- **URL**: [https://core.telegram.org/bots/api#videonote](https://core.telegram.org/bots/api#videonote)
- **Description**:
  - This object represents a video message (available in Telegram apps as of v.4.0).
- **Fields**:
  - **file_id**: String (Required: True)
    - Identifier for this file, which can be used to download or reuse the file
  - **file_unique_id**: String (Required: True)
    - Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
  - **length**: Integer (Required: True)
    - Video width and height (diameter of the video message) as defined by the sender
  - **duration**: Integer (Required: True)
    - Duration of the video in seconds as defined by the sender
  - **thumbnail**: PhotoSize (Required: False)
    - Optional. Video thumbnail
  - **file_size**: Integer (Required: False)
    - Optional. File size in bytes

💡 --- 💡

### 📦 Voice <a id='voice'></a>
- **URL**: [https://core.telegram.org/bots/api#voice](https://core.telegram.org/bots/api#voice)
- **Description**:
  - This object represents a voice note.
- **Fields**:
  - **file_id**: String (Required: True)
    - Identifier for this file, which can be used to download or reuse the file
  - **file_unique_id**: String (Required: True)
    - Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
  - **duration**: Integer (Required: True)
    - Duration of the audio in seconds as defined by the sender
  - **mime_type**: String (Required: False)
    - Optional. MIME type of the file as defined by the sender
  - **file_size**: Integer (Required: False)
    - Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.

💡 --- 💡

### 📦 PaidMediaInfo <a id='paidmediainfo'></a>
- **URL**: [https://core.telegram.org/bots/api#paidmediainfo](https://core.telegram.org/bots/api#paidmediainfo)
- **Description**:
  - Describes the paid media added to a message.
- **Fields**:
  - **star_count**: Integer (Required: True)
    - The number of Telegram Stars that must be paid to buy access to the media
  - **paid_media**: Array of PaidMedia (Required: True)
    - Information about the paid media

💡 --- 💡

### 📦 PaidMedia <a id='paidmedia'></a>
- **URL**: [https://core.telegram.org/bots/api#paidmedia](https://core.telegram.org/bots/api#paidmedia)
- **Description**:
  - This object describes paid media. Currently, it can be one of
  - - PaidMediaPreview
  - - PaidMediaPhoto
  - - PaidMediaVideo
- **Subtypes**:
  - PaidMediaPreview
  - PaidMediaPhoto
  - PaidMediaVideo

💡 --- 💡

### 📦 PaidMediaPreview <a id='paidmediapreview'></a>
- **URL**: [https://core.telegram.org/bots/api#paidmediapreview](https://core.telegram.org/bots/api#paidmediapreview)
- **Description**:
  - The paid media isn't available before the payment.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the paid media, always "preview"
  - **width**: Integer (Required: False)
    - Optional. Media width as defined by the sender
  - **height**: Integer (Required: False)
    - Optional. Media height as defined by the sender
  - **duration**: Integer (Required: False)
    - Optional. Duration of the media in seconds as defined by the sender

💡 --- 💡

### 📦 PaidMediaPhoto <a id='paidmediaphoto'></a>
- **URL**: [https://core.telegram.org/bots/api#paidmediaphoto](https://core.telegram.org/bots/api#paidmediaphoto)
- **Description**:
  - The paid media is a photo.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the paid media, always "photo"
  - **photo**: Array of PhotoSize (Required: True)
    - The photo

💡 --- 💡

### 📦 PaidMediaVideo <a id='paidmediavideo'></a>
- **URL**: [https://core.telegram.org/bots/api#paidmediavideo](https://core.telegram.org/bots/api#paidmediavideo)
- **Description**:
  - The paid media is a video.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the paid media, always "video"
  - **video**: Video (Required: True)
    - The video

💡 --- 💡

### 📦 Contact <a id='contact'></a>
- **URL**: [https://core.telegram.org/bots/api#contact](https://core.telegram.org/bots/api#contact)
- **Description**:
  - This object represents a phone contact.
- **Fields**:
  - **phone_number**: String (Required: True)
    - Contact's phone number
  - **first_name**: String (Required: True)
    - Contact's first name
  - **last_name**: String (Required: False)
    - Optional. Contact's last name
  - **user_id**: Integer (Required: False)
    - Optional. Contact's user identifier in Telegram. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
  - **vcard**: String (Required: False)
    - Optional. Additional data about the contact in the form of a vCard

💡 --- 💡

### 📦 Dice <a id='dice'></a>
- **URL**: [https://core.telegram.org/bots/api#dice](https://core.telegram.org/bots/api#dice)
- **Description**:
  - This object represents an animated emoji that displays a random value.
- **Fields**:
  - **emoji**: String (Required: True)
    - Emoji on which the dice throw animation is based
  - **value**: Integer (Required: True)
    - Value of the dice, 1-6 for "🎲", "🎯" and "🎳" base emoji, 1-5 for "🏀" and "⚽" base emoji, 1-64 for "🎰" base emoji

💡 --- 💡

### 📦 PollOption <a id='polloption'></a>
- **URL**: [https://core.telegram.org/bots/api#polloption](https://core.telegram.org/bots/api#polloption)
- **Description**:
  - This object contains information about one answer option in a poll.
- **Fields**:
  - **text**: String (Required: True)
    - Option text, 1-100 characters
  - **text_entities**: Array of MessageEntity (Required: False)
    - Optional. Special entities that appear in the option text. Currently, only custom emoji entities are allowed in poll option texts
  - **voter_count**: Integer (Required: True)
    - Number of users that voted for this option

💡 --- 💡

### 📦 InputPollOption <a id='inputpolloption'></a>
- **URL**: [https://core.telegram.org/bots/api#inputpolloption](https://core.telegram.org/bots/api#inputpolloption)
- **Description**:
  - This object contains information about one answer option in a poll to be sent.
- **Fields**:
  - **text**: String (Required: True)
    - Option text, 1-100 characters
  - **text_parse_mode**: String (Required: False)
    - Optional. Mode for parsing entities in the text. See formatting options for more details. Currently, only custom emoji entities are allowed
  - **text_entities**: Array of MessageEntity (Required: False)
    - Optional. A JSON-serialized list of special entities that appear in the poll option text. It can be specified instead of text_parse_mode

💡 --- 💡

### 📦 PollAnswer <a id='pollanswer'></a>
- **URL**: [https://core.telegram.org/bots/api#pollanswer](https://core.telegram.org/bots/api#pollanswer)
- **Description**:
  - This object represents an answer of a user in a non-anonymous poll.
- **Fields**:
  - **poll_id**: String (Required: True)
    - Unique poll identifier
  - **voter_chat**: Chat (Required: False)
    - Optional. The chat that changed the answer to the poll, if the voter is anonymous
  - **user**: User (Required: False)
    - Optional. The user that changed the answer to the poll, if the voter isn't anonymous
  - **option_ids**: Array of Integer (Required: True)
    - 0-based identifiers of chosen answer options. May be empty if the vote was retracted.

💡 --- 💡

### 📦 Poll <a id='poll'></a>
- **URL**: [https://core.telegram.org/bots/api#poll](https://core.telegram.org/bots/api#poll)
- **Description**:
  - This object contains information about a poll.
- **Fields**:
  - **id**: String (Required: True)
    - Unique poll identifier
  - **question**: String (Required: True)
    - Poll question, 1-300 characters
  - **question_entities**: Array of MessageEntity (Required: False)
    - Optional. Special entities that appear in the question. Currently, only custom emoji entities are allowed in poll questions
  - **options**: Array of PollOption (Required: True)
    - List of poll options
  - **total_voter_count**: Integer (Required: True)
    - Total number of users that voted in the poll
  - **is_closed**: Boolean (Required: True)
    - True, if the poll is closed
  - **is_anonymous**: Boolean (Required: True)
    - True, if the poll is anonymous
  - **type**: String (Required: True)
    - Poll type, currently can be "regular" or "quiz"
  - **allows_multiple_answers**: Boolean (Required: True)
    - True, if the poll allows multiple answers
  - **correct_option_id**: Integer (Required: False)
    - Optional. 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot.
  - **explanation**: String (Required: False)
    - Optional. Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters
  - **explanation_entities**: Array of MessageEntity (Required: False)
    - Optional. Special entities like usernames, URLs, bot commands, etc. that appear in the explanation
  - **open_period**: Integer (Required: False)
    - Optional. Amount of time in seconds the poll will be active after creation
  - **close_date**: Integer (Required: False)
    - Optional. Point in time (Unix timestamp) when the poll will be automatically closed

💡 --- 💡

### 📦 Location <a id='location'></a>
- **URL**: [https://core.telegram.org/bots/api#location](https://core.telegram.org/bots/api#location)
- **Description**:
  - This object represents a point on the map.
- **Fields**:
  - **latitude**: Float (Required: True)
    - Latitude as defined by the sender
  - **longitude**: Float (Required: True)
    - Longitude as defined by the sender
  - **horizontal_accuracy**: Float (Required: False)
    - Optional. The radius of uncertainty for the location, measured in meters; 0-1500
  - **live_period**: Integer (Required: False)
    - Optional. Time relative to the message sending date, during which the location can be updated; in seconds. For active live locations only.
  - **heading**: Integer (Required: False)
    - Optional. The direction in which user is moving, in degrees; 1-360. For active live locations only.
  - **proximity_alert_radius**: Integer (Required: False)
    - Optional. The maximum distance for proximity alerts about approaching another chat member, in meters. For sent live locations only.

💡 --- 💡

### 📦 Venue <a id='venue'></a>
- **URL**: [https://core.telegram.org/bots/api#venue](https://core.telegram.org/bots/api#venue)
- **Description**:
  - This object represents a venue.
- **Fields**:
  - **location**: Location (Required: True)
    - Venue location. Can't be a live location
  - **title**: String (Required: True)
    - Name of the venue
  - **address**: String (Required: True)
    - Address of the venue
  - **foursquare_id**: String (Required: False)
    - Optional. Foursquare identifier of the venue
  - **foursquare_type**: String (Required: False)
    - Optional. Foursquare type of the venue. (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".)
  - **google_place_id**: String (Required: False)
    - Optional. Google Places identifier of the venue
  - **google_place_type**: String (Required: False)
    - Optional. Google Places type of the venue. (See supported types.)

💡 --- 💡

### 📦 WebAppData <a id='webappdata'></a>
- **URL**: [https://core.telegram.org/bots/api#webappdata](https://core.telegram.org/bots/api#webappdata)
- **Description**:
  - Describes data sent from a Web App to the bot.
- **Fields**:
  - **data**: String (Required: True)
    - The data. Be aware that a bad client can send arbitrary data in this field.
  - **button_text**: String (Required: True)
    - Text of the web_app keyboard button from which the Web App was opened. Be aware that a bad client can send arbitrary data in this field.

💡 --- 💡

### 📦 ProximityAlertTriggered <a id='proximityalerttriggered'></a>
- **URL**: [https://core.telegram.org/bots/api#proximityalerttriggered](https://core.telegram.org/bots/api#proximityalerttriggered)
- **Description**:
  - This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user.
- **Fields**:
  - **traveler**: User (Required: True)
    - User that triggered the alert
  - **watcher**: User (Required: True)
    - User that set the alert
  - **distance**: Integer (Required: True)
    - The distance between the users

💡 --- 💡

### 📦 MessageAutoDeleteTimerChanged <a id='messageautodeletetimerchanged'></a>
- **URL**: [https://core.telegram.org/bots/api#messageautodeletetimerchanged](https://core.telegram.org/bots/api#messageautodeletetimerchanged)
- **Description**:
  - This object represents a service message about a change in auto-delete timer settings.
- **Fields**:
  - **message_auto_delete_time**: Integer (Required: True)
    - New auto-delete time for messages in the chat; in seconds

💡 --- 💡

### 📦 ChatBoostAdded <a id='chatboostadded'></a>
- **URL**: [https://core.telegram.org/bots/api#chatboostadded](https://core.telegram.org/bots/api#chatboostadded)
- **Description**:
  - This object represents a service message about a user boosting a chat.
- **Fields**:
  - **boost_count**: Integer (Required: True)
    - Number of boosts added by the user

💡 --- 💡

### 📦 BackgroundFill <a id='backgroundfill'></a>
- **URL**: [https://core.telegram.org/bots/api#backgroundfill](https://core.telegram.org/bots/api#backgroundfill)
- **Description**:
  - This object describes the way a background is filled based on the selected colors. Currently, it can be one of
  - - BackgroundFillSolid
  - - BackgroundFillGradient
  - - BackgroundFillFreeformGradient
- **Subtypes**:
  - BackgroundFillSolid
  - BackgroundFillGradient
  - BackgroundFillFreeformGradient

💡 --- 💡

### 📦 BackgroundFillSolid <a id='backgroundfillsolid'></a>
- **URL**: [https://core.telegram.org/bots/api#backgroundfillsolid](https://core.telegram.org/bots/api#backgroundfillsolid)
- **Description**:
  - The background is filled using the selected color.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the background fill, always "solid"
  - **color**: Integer (Required: True)
    - The color of the background fill in the RGB24 format

💡 --- 💡

### 📦 BackgroundFillGradient <a id='backgroundfillgradient'></a>
- **URL**: [https://core.telegram.org/bots/api#backgroundfillgradient](https://core.telegram.org/bots/api#backgroundfillgradient)
- **Description**:
  - The background is a gradient fill.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the background fill, always "gradient"
  - **top_color**: Integer (Required: True)
    - Top color of the gradient in the RGB24 format
  - **bottom_color**: Integer (Required: True)
    - Bottom color of the gradient in the RGB24 format
  - **rotation_angle**: Integer (Required: True)
    - Clockwise rotation angle of the background fill in degrees; 0-359

💡 --- 💡

### 📦 BackgroundFillFreeformGradient <a id='backgroundfillfreeformgradient'></a>
- **URL**: [https://core.telegram.org/bots/api#backgroundfillfreeformgradient](https://core.telegram.org/bots/api#backgroundfillfreeformgradient)
- **Description**:
  - The background is a freeform gradient that rotates after every message in the chat.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the background fill, always "freeform_gradient"
  - **colors**: Array of Integer (Required: True)
    - A list of the 3 or 4 base colors that are used to generate the freeform gradient in the RGB24 format

💡 --- 💡

### 📦 BackgroundType <a id='backgroundtype'></a>
- **URL**: [https://core.telegram.org/bots/api#backgroundtype](https://core.telegram.org/bots/api#backgroundtype)
- **Description**:
  - This object describes the type of a background. Currently, it can be one of
  - - BackgroundTypeFill
  - - BackgroundTypeWallpaper
  - - BackgroundTypePattern
  - - BackgroundTypeChatTheme
- **Subtypes**:
  - BackgroundTypeFill
  - BackgroundTypeWallpaper
  - BackgroundTypePattern
  - BackgroundTypeChatTheme

💡 --- 💡

### 📦 BackgroundTypeFill <a id='backgroundtypefill'></a>
- **URL**: [https://core.telegram.org/bots/api#backgroundtypefill](https://core.telegram.org/bots/api#backgroundtypefill)
- **Description**:
  - The background is automatically filled based on the selected colors.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the background, always "fill"
  - **fill**: BackgroundFill (Required: True)
    - The background fill
  - **dark_theme_dimming**: Integer (Required: True)
    - Dimming of the background in dark themes, as a percentage; 0-100

💡 --- 💡

### 📦 BackgroundTypeWallpaper <a id='backgroundtypewallpaper'></a>
- **URL**: [https://core.telegram.org/bots/api#backgroundtypewallpaper](https://core.telegram.org/bots/api#backgroundtypewallpaper)
- **Description**:
  - The background is a wallpaper in the JPEG format.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the background, always "wallpaper"
  - **document**: Document (Required: True)
    - Document with the wallpaper
  - **dark_theme_dimming**: Integer (Required: True)
    - Dimming of the background in dark themes, as a percentage; 0-100
  - **is_blurred**: Boolean (Required: False)
    - Optional. True, if the wallpaper is downscaled to fit in a 450x450 square and then box-blurred with radius 12
  - **is_moving**: Boolean (Required: False)
    - Optional. True, if the background moves slightly when the device is tilted

💡 --- 💡

### 📦 BackgroundTypePattern <a id='backgroundtypepattern'></a>
- **URL**: [https://core.telegram.org/bots/api#backgroundtypepattern](https://core.telegram.org/bots/api#backgroundtypepattern)
- **Description**:
  - The background is a PNG or TGV (gzipped subset of SVG with MIME type "application/x-tgwallpattern") pattern to be combined with the background fill chosen by the user.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the background, always "pattern"
  - **document**: Document (Required: True)
    - Document with the pattern
  - **fill**: BackgroundFill (Required: True)
    - The background fill that is combined with the pattern
  - **intensity**: Integer (Required: True)
    - Intensity of the pattern when it is shown above the filled background; 0-100
  - **is_inverted**: Boolean (Required: False)
    - Optional. True, if the background fill must be applied only to the pattern itself. All other pixels are black in this case. For dark themes only
  - **is_moving**: Boolean (Required: False)
    - Optional. True, if the background moves slightly when the device is tilted

💡 --- 💡

### 📦 BackgroundTypeChatTheme <a id='backgroundtypechattheme'></a>
- **URL**: [https://core.telegram.org/bots/api#backgroundtypechattheme](https://core.telegram.org/bots/api#backgroundtypechattheme)
- **Description**:
  - The background is taken directly from a built-in chat theme.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the background, always "chat_theme"
  - **theme_name**: String (Required: True)
    - Name of the chat theme, which is usually an emoji

💡 --- 💡

### 📦 ChatBackground <a id='chatbackground'></a>
- **URL**: [https://core.telegram.org/bots/api#chatbackground](https://core.telegram.org/bots/api#chatbackground)
- **Description**:
  - This object represents a chat background.
- **Fields**:
  - **type**: BackgroundType (Required: True)
    - Type of the background

💡 --- 💡

### 📦 ForumTopicCreated <a id='forumtopiccreated'></a>
- **URL**: [https://core.telegram.org/bots/api#forumtopiccreated](https://core.telegram.org/bots/api#forumtopiccreated)
- **Description**:
  - This object represents a service message about a new forum topic created in the chat.
- **Fields**:
  - **name**: String (Required: True)
    - Name of the topic
  - **icon_color**: Integer (Required: True)
    - Color of the topic icon in RGB format
  - **icon_custom_emoji_id**: String (Required: False)
    - Optional. Unique identifier of the custom emoji shown as the topic icon

💡 --- 💡

### 📦 ForumTopicClosed <a id='forumtopicclosed'></a>
- **URL**: [https://core.telegram.org/bots/api#forumtopicclosed](https://core.telegram.org/bots/api#forumtopicclosed)
- **Description**:
  - This object represents a service message about a forum topic closed in the chat. Currently holds no information.

💡 --- 💡

### 📦 ForumTopicEdited <a id='forumtopicedited'></a>
- **URL**: [https://core.telegram.org/bots/api#forumtopicedited](https://core.telegram.org/bots/api#forumtopicedited)
- **Description**:
  - This object represents a service message about an edited forum topic.
- **Fields**:
  - **name**: String (Required: False)
    - Optional. New name of the topic, if it was edited
  - **icon_custom_emoji_id**: String (Required: False)
    - Optional. New identifier of the custom emoji shown as the topic icon, if it was edited; an empty string if the icon was removed

💡 --- 💡

### 📦 ForumTopicReopened <a id='forumtopicreopened'></a>
- **URL**: [https://core.telegram.org/bots/api#forumtopicreopened](https://core.telegram.org/bots/api#forumtopicreopened)
- **Description**:
  - This object represents a service message about a forum topic reopened in the chat. Currently holds no information.

💡 --- 💡

### 📦 GeneralForumTopicHidden <a id='generalforumtopichidden'></a>
- **URL**: [https://core.telegram.org/bots/api#generalforumtopichidden](https://core.telegram.org/bots/api#generalforumtopichidden)
- **Description**:
  - This object represents a service message about General forum topic hidden in the chat. Currently holds no information.

💡 --- 💡

### 📦 GeneralForumTopicUnhidden <a id='generalforumtopicunhidden'></a>
- **URL**: [https://core.telegram.org/bots/api#generalforumtopicunhidden](https://core.telegram.org/bots/api#generalforumtopicunhidden)
- **Description**:
  - This object represents a service message about General forum topic unhidden in the chat. Currently holds no information.

💡 --- 💡

### 📦 SharedUser <a id='shareduser'></a>
- **URL**: [https://core.telegram.org/bots/api#shareduser](https://core.telegram.org/bots/api#shareduser)
- **Description**:
  - This object contains information about a user that was shared with the bot using a KeyboardButtonRequestUsers button.
- **Fields**:
  - **user_id**: Integer (Required: True)
    - Identifier of the shared user. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so 64-bit integers or double-precision float types are safe for storing these identifiers. The bot may not have access to the user and could be unable to use this identifier, unless the user is already known to the bot by some other means.
  - **first_name**: String (Required: False)
    - Optional. First name of the user, if the name was requested by the bot
  - **last_name**: String (Required: False)
    - Optional. Last name of the user, if the name was requested by the bot
  - **username**: String (Required: False)
    - Optional. Username of the user, if the username was requested by the bot
  - **photo**: Array of PhotoSize (Required: False)
    - Optional. Available sizes of the chat photo, if the photo was requested by the bot

💡 --- 💡

### 📦 UsersShared <a id='usersshared'></a>
- **URL**: [https://core.telegram.org/bots/api#usersshared](https://core.telegram.org/bots/api#usersshared)
- **Description**:
  - This object contains information about the users whose identifiers were shared with the bot using a KeyboardButtonRequestUsers button.
- **Fields**:
  - **request_id**: Integer (Required: True)
    - Identifier of the request
  - **users**: Array of SharedUser (Required: True)
    - Information about users shared with the bot.

💡 --- 💡

### 📦 ChatShared <a id='chatshared'></a>
- **URL**: [https://core.telegram.org/bots/api#chatshared](https://core.telegram.org/bots/api#chatshared)
- **Description**:
  - This object contains information about a chat that was shared with the bot using a KeyboardButtonRequestChat button.
- **Fields**:
  - **request_id**: Integer (Required: True)
    - Identifier of the request
  - **chat_id**: Integer (Required: True)
    - Identifier of the shared chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot may not have access to the chat and could be unable to use this identifier, unless the chat is already known to the bot by some other means.
  - **title**: String (Required: False)
    - Optional. Title of the chat, if the title was requested by the bot.
  - **username**: String (Required: False)
    - Optional. Username of the chat, if the username was requested by the bot and available.
  - **photo**: Array of PhotoSize (Required: False)
    - Optional. Available sizes of the chat photo, if the photo was requested by the bot

💡 --- 💡

### 📦 WriteAccessAllowed <a id='writeaccessallowed'></a>
- **URL**: [https://core.telegram.org/bots/api#writeaccessallowed](https://core.telegram.org/bots/api#writeaccessallowed)
- **Description**:
  - This object represents a service message about a user allowing a bot to write messages after adding it to the attachment menu, launching a Web App from a link, or accepting an explicit request from a Web App sent by the method requestWriteAccess.
- **Fields**:
  - **from_request**: Boolean (Required: False)
    - Optional. True, if the access was granted after the user accepted an explicit request from a Web App sent by the method requestWriteAccess
  - **web_app_name**: String (Required: False)
    - Optional. Name of the Web App, if the access was granted when the Web App was launched from a link
  - **from_attachment_menu**: Boolean (Required: False)
    - Optional. True, if the access was granted when the bot was added to the attachment or side menu

💡 --- 💡

### 📦 VideoChatScheduled <a id='videochatscheduled'></a>
- **URL**: [https://core.telegram.org/bots/api#videochatscheduled](https://core.telegram.org/bots/api#videochatscheduled)
- **Description**:
  - This object represents a service message about a video chat scheduled in the chat.
- **Fields**:
  - **start_date**: Integer (Required: True)
    - Point in time (Unix timestamp) when the video chat is supposed to be started by a chat administrator

💡 --- 💡

### 📦 VideoChatStarted <a id='videochatstarted'></a>
- **URL**: [https://core.telegram.org/bots/api#videochatstarted](https://core.telegram.org/bots/api#videochatstarted)
- **Description**:
  - This object represents a service message about a video chat started in the chat. Currently holds no information.

💡 --- 💡

### 📦 VideoChatEnded <a id='videochatended'></a>
- **URL**: [https://core.telegram.org/bots/api#videochatended](https://core.telegram.org/bots/api#videochatended)
- **Description**:
  - This object represents a service message about a video chat ended in the chat.
- **Fields**:
  - **duration**: Integer (Required: True)
    - Video chat duration in seconds

💡 --- 💡

### 📦 VideoChatParticipantsInvited <a id='videochatparticipantsinvited'></a>
- **URL**: [https://core.telegram.org/bots/api#videochatparticipantsinvited](https://core.telegram.org/bots/api#videochatparticipantsinvited)
- **Description**:
  - This object represents a service message about new members invited to a video chat.
- **Fields**:
  - **users**: Array of User (Required: True)
    - New members that were invited to the video chat

💡 --- 💡

### 📦 GiveawayCreated <a id='giveawaycreated'></a>
- **URL**: [https://core.telegram.org/bots/api#giveawaycreated](https://core.telegram.org/bots/api#giveawaycreated)
- **Description**:
  - This object represents a service message about the creation of a scheduled giveaway.
- **Fields**:
  - **prize_star_count**: Integer (Required: False)
    - Optional. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only

💡 --- 💡

### 📦 Giveaway <a id='giveaway'></a>
- **URL**: [https://core.telegram.org/bots/api#giveaway](https://core.telegram.org/bots/api#giveaway)
- **Description**:
  - This object represents a message about a scheduled giveaway.
- **Fields**:
  - **chats**: Array of Chat (Required: True)
    - The list of chats which the user must join to participate in the giveaway
  - **winners_selection_date**: Integer (Required: True)
    - Point in time (Unix timestamp) when winners of the giveaway will be selected
  - **winner_count**: Integer (Required: True)
    - The number of users which are supposed to be selected as winners of the giveaway
  - **only_new_members**: Boolean (Required: False)
    - Optional. True, if only users who join the chats after the giveaway started should be eligible to win
  - **has_public_winners**: Boolean (Required: False)
    - Optional. True, if the list of giveaway winners will be visible to everyone
  - **prize_description**: String (Required: False)
    - Optional. Description of additional giveaway prize
  - **country_codes**: Array of String (Required: False)
    - Optional. A list of two-letter ISO 3166-1 alpha-2 country codes indicating the countries from which eligible users for the giveaway must come. If empty, then all users can participate in the giveaway. Users with a phone number that was bought on Fragment can always participate in giveaways.
  - **prize_star_count**: Integer (Required: False)
    - Optional. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only
  - **premium_subscription_month_count**: Integer (Required: False)
    - Optional. The number of months the Telegram Premium subscription won from the giveaway will be active for; for Telegram Premium giveaways only

💡 --- 💡

### 📦 GiveawayWinners <a id='giveawaywinners'></a>
- **URL**: [https://core.telegram.org/bots/api#giveawaywinners](https://core.telegram.org/bots/api#giveawaywinners)
- **Description**:
  - This object represents a message about the completion of a giveaway with public winners.
- **Fields**:
  - **chat**: Chat (Required: True)
    - The chat that created the giveaway
  - **giveaway_message_id**: Integer (Required: True)
    - Identifier of the message with the giveaway in the chat
  - **winners_selection_date**: Integer (Required: True)
    - Point in time (Unix timestamp) when winners of the giveaway were selected
  - **winner_count**: Integer (Required: True)
    - Total number of winners in the giveaway
  - **winners**: Array of User (Required: True)
    - List of up to 100 winners of the giveaway
  - **additional_chat_count**: Integer (Required: False)
    - Optional. The number of other chats the user had to join in order to be eligible for the giveaway
  - **prize_star_count**: Integer (Required: False)
    - Optional. The number of Telegram Stars that were split between giveaway winners; for Telegram Star giveaways only
  - **premium_subscription_month_count**: Integer (Required: False)
    - Optional. The number of months the Telegram Premium subscription won from the giveaway will be active for; for Telegram Premium giveaways only
  - **unclaimed_prize_count**: Integer (Required: False)
    - Optional. Number of undistributed prizes
  - **only_new_members**: Boolean (Required: False)
    - Optional. True, if only users who had joined the chats after the giveaway started were eligible to win
  - **was_refunded**: Boolean (Required: False)
    - Optional. True, if the giveaway was canceled because the payment for it was refunded
  - **prize_description**: String (Required: False)
    - Optional. Description of additional giveaway prize

💡 --- 💡

### 📦 GiveawayCompleted <a id='giveawaycompleted'></a>
- **URL**: [https://core.telegram.org/bots/api#giveawaycompleted](https://core.telegram.org/bots/api#giveawaycompleted)
- **Description**:
  - This object represents a service message about the completion of a giveaway without public winners.
- **Fields**:
  - **winner_count**: Integer (Required: True)
    - Number of winners in the giveaway
  - **unclaimed_prize_count**: Integer (Required: False)
    - Optional. Number of undistributed prizes
  - **giveaway_message**: Message (Required: False)
    - Optional. Message with the giveaway that was completed, if it wasn't deleted
  - **is_star_giveaway**: Boolean (Required: False)
    - Optional. True, if the giveaway is a Telegram Star giveaway. Otherwise, currently, the giveaway is a Telegram Premium giveaway.

💡 --- 💡

### 📦 LinkPreviewOptions <a id='linkpreviewoptions'></a>
- **URL**: [https://core.telegram.org/bots/api#linkpreviewoptions](https://core.telegram.org/bots/api#linkpreviewoptions)
- **Description**:
  - Describes the options used for link preview generation.
- **Fields**:
  - **is_disabled**: Boolean (Required: False)
    - Optional. True, if the link preview is disabled
  - **url**: String (Required: False)
    - Optional. URL to use for the link preview. If empty, then the first URL found in the message text will be used
  - **prefer_small_media**: Boolean (Required: False)
    - Optional. True, if the media in the link preview is supposed to be shrunk; ignored if the URL isn't explicitly specified or media size change isn't supported for the preview
  - **prefer_large_media**: Boolean (Required: False)
    - Optional. True, if the media in the link preview is supposed to be enlarged; ignored if the URL isn't explicitly specified or media size change isn't supported for the preview
  - **show_above_text**: Boolean (Required: False)
    - Optional. True, if the link preview must be shown above the message text; otherwise, the link preview will be shown below the message text

💡 --- 💡

### 📦 UserProfilePhotos <a id='userprofilephotos'></a>
- **URL**: [https://core.telegram.org/bots/api#userprofilephotos](https://core.telegram.org/bots/api#userprofilephotos)
- **Description**:
  - This object represent a user's profile pictures.
- **Fields**:
  - **total_count**: Integer (Required: True)
    - Total number of profile pictures the target user has
  - **photos**: Array of Array of PhotoSize (Required: True)
    - Requested profile pictures (in up to 4 sizes each)

💡 --- 💡

### 📦 File <a id='file'></a>
- **URL**: [https://core.telegram.org/bots/api#file](https://core.telegram.org/bots/api#file)
- **Description**:
  - This object represents a file ready to be downloaded. The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile.
- **Fields**:
  - **file_id**: String (Required: True)
    - Identifier for this file, which can be used to download or reuse the file
  - **file_unique_id**: String (Required: True)
    - Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
  - **file_size**: Integer (Required: False)
    - Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
  - **file_path**: String (Required: False)
    - Optional. File path. Use https://api.telegram.org/file/bot<token>/<file_path> to get the file.

💡 --- 💡

### 📦 WebAppInfo <a id='webappinfo'></a>
- **URL**: [https://core.telegram.org/bots/api#webappinfo](https://core.telegram.org/bots/api#webappinfo)
- **Description**:
  - Describes a Web App.
- **Fields**:
  - **url**: String (Required: True)
    - An HTTPS URL of a Web App to be opened with additional data as specified in Initializing Web Apps

💡 --- 💡

### 📦 ReplyKeyboardMarkup <a id='replykeyboardmarkup'></a>
- **URL**: [https://core.telegram.org/bots/api#replykeyboardmarkup](https://core.telegram.org/bots/api#replykeyboardmarkup)
- **Description**:
  - This object represents a custom keyboard with reply options (see Introduction to bots for details and examples). Not supported in channels and for messages sent on behalf of a Telegram Business account.
- **Fields**:
  - **keyboard**: Array of Array of KeyboardButton (Required: True)
    - Array of button rows, each represented by an Array of KeyboardButton objects
  - **is_persistent**: Boolean (Required: False)
    - Optional. Requests clients to always show the keyboard when the regular keyboard is hidden. Defaults to false, in which case the custom keyboard can be hidden and opened with a keyboard icon.
  - **resize_keyboard**: Boolean (Required: False)
    - Optional. Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if there are just two rows of buttons). Defaults to false, in which case the custom keyboard is always of the same height as the app's standard keyboard.
  - **one_time_keyboard**: Boolean (Required: False)
    - Optional. Requests clients to hide the keyboard as soon as it's been used. The keyboard will still be available, but clients will automatically display the usual letter-keyboard in the chat - the user can press a special button in the input field to see the custom keyboard again. Defaults to false.
  - **input_field_placeholder**: String (Required: False)
    - Optional. The placeholder to be shown in the input field when the keyboard is active; 1-64 characters
  - **selective**: Boolean (Required: False)
    - Optional. Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply to a message in the same chat and forum topic, sender of the original message. Example: A user requests to change the bot's language, bot replies to the request with a keyboard to select the new language. Other users in the group don't see the keyboard.

💡 --- 💡

### 📦 KeyboardButton <a id='keyboardbutton'></a>
- **URL**: [https://core.telegram.org/bots/api#keyboardbutton](https://core.telegram.org/bots/api#keyboardbutton)
- **Description**:
  - This object represents one button of the reply keyboard. At most one of the optional fields must be used to specify type of the button. For simple text buttons, String can be used instead of this object to specify the button text.
  - Note: request_users and request_chat options will only work in Telegram versions released after 3 February, 2023. Older clients will display unsupported message.
- **Fields**:
  - **text**: String (Required: True)
    - Text of the button. If none of the optional fields are used, it will be sent as a message when the button is pressed
  - **request_users**: KeyboardButtonRequestUsers (Required: False)
    - Optional. If specified, pressing the button will open a list of suitable users. Identifiers of selected users will be sent to the bot in a "users_shared" service message. Available in private chats only.
  - **request_chat**: KeyboardButtonRequestChat (Required: False)
    - Optional. If specified, pressing the button will open a list of suitable chats. Tapping on a chat will send its identifier to the bot in a "chat_shared" service message. Available in private chats only.
  - **request_contact**: Boolean (Required: False)
    - Optional. If True, the user's phone number will be sent as a contact when the button is pressed. Available in private chats only.
  - **request_location**: Boolean (Required: False)
    - Optional. If True, the user's current location will be sent when the button is pressed. Available in private chats only.
  - **request_poll**: KeyboardButtonPollType (Required: False)
    - Optional. If specified, the user will be asked to create a poll and send it to the bot when the button is pressed. Available in private chats only.
  - **web_app**: WebAppInfo (Required: False)
    - Optional. If specified, the described Web App will be launched when the button is pressed. The Web App will be able to send a "web_app_data" service message. Available in private chats only.

💡 --- 💡

### 📦 KeyboardButtonRequestUsers <a id='keyboardbuttonrequestusers'></a>
- **URL**: [https://core.telegram.org/bots/api#keyboardbuttonrequestusers](https://core.telegram.org/bots/api#keyboardbuttonrequestusers)
- **Description**:
  - This object defines the criteria used to request suitable users. Information about the selected users will be shared with the bot when the corresponding button is pressed. More about requesting users: https://core.telegram.org/bots/features#chat-and-user-selection
- **Fields**:
  - **request_id**: Integer (Required: True)
    - Signed 32-bit identifier of the request that will be received back in the UsersShared object. Must be unique within the message
  - **user_is_bot**: Boolean (Required: False)
    - Optional. Pass True to request bots, pass False to request regular users. If not specified, no additional restrictions are applied.
  - **user_is_premium**: Boolean (Required: False)
    - Optional. Pass True to request premium users, pass False to request non-premium users. If not specified, no additional restrictions are applied.
  - **max_quantity**: Integer (Required: False)
    - Optional. The maximum number of users to be selected; 1-10. Defaults to 1.
  - **request_name**: Boolean (Required: False)
    - Optional. Pass True to request the users' first and last names
  - **request_username**: Boolean (Required: False)
    - Optional. Pass True to request the users' usernames
  - **request_photo**: Boolean (Required: False)
    - Optional. Pass True to request the users' photos

💡 --- 💡

### 📦 KeyboardButtonRequestChat <a id='keyboardbuttonrequestchat'></a>
- **URL**: [https://core.telegram.org/bots/api#keyboardbuttonrequestchat](https://core.telegram.org/bots/api#keyboardbuttonrequestchat)
- **Description**:
  - This object defines the criteria used to request a suitable chat. Information about the selected chat will be shared with the bot when the corresponding button is pressed. The bot will be granted requested rights in the chat if appropriate. More about requesting chats: https://core.telegram.org/bots/features#chat-and-user-selection.
- **Fields**:
  - **request_id**: Integer (Required: True)
    - Signed 32-bit identifier of the request, which will be received back in the ChatShared object. Must be unique within the message
  - **chat_is_channel**: Boolean (Required: True)
    - Pass True to request a channel chat, pass False to request a group or a supergroup chat.
  - **chat_is_forum**: Boolean (Required: False)
    - Optional. Pass True to request a forum supergroup, pass False to request a non-forum chat. If not specified, no additional restrictions are applied.
  - **chat_has_username**: Boolean (Required: False)
    - Optional. Pass True to request a supergroup or a channel with a username, pass False to request a chat without a username. If not specified, no additional restrictions are applied.
  - **chat_is_created**: Boolean (Required: False)
    - Optional. Pass True to request a chat owned by the user. Otherwise, no additional restrictions are applied.
  - **user_administrator_rights**: ChatAdministratorRights (Required: False)
    - Optional. A JSON-serialized object listing the required administrator rights of the user in the chat. The rights must be a superset of bot_administrator_rights. If not specified, no additional restrictions are applied.
  - **bot_administrator_rights**: ChatAdministratorRights (Required: False)
    - Optional. A JSON-serialized object listing the required administrator rights of the bot in the chat. The rights must be a subset of user_administrator_rights. If not specified, no additional restrictions are applied.
  - **bot_is_member**: Boolean (Required: False)
    - Optional. Pass True to request a chat with the bot as a member. Otherwise, no additional restrictions are applied.
  - **request_title**: Boolean (Required: False)
    - Optional. Pass True to request the chat's title
  - **request_username**: Boolean (Required: False)
    - Optional. Pass True to request the chat's username
  - **request_photo**: Boolean (Required: False)
    - Optional. Pass True to request the chat's photo

💡 --- 💡

### 📦 KeyboardButtonPollType <a id='keyboardbuttonpolltype'></a>
- **URL**: [https://core.telegram.org/bots/api#keyboardbuttonpolltype](https://core.telegram.org/bots/api#keyboardbuttonpolltype)
- **Description**:
  - This object represents type of a poll, which is allowed to be created and sent when the corresponding button is pressed.
- **Fields**:
  - **type**: String (Required: False)
    - Optional. If quiz is passed, the user will be allowed to create only polls in the quiz mode. If regular is passed, only regular polls will be allowed. Otherwise, the user will be allowed to create a poll of any type.

💡 --- 💡

### 📦 ReplyKeyboardRemove <a id='replykeyboardremove'></a>
- **URL**: [https://core.telegram.org/bots/api#replykeyboardremove](https://core.telegram.org/bots/api#replykeyboardremove)
- **Description**:
  - Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup). Not supported in channels and for messages sent on behalf of a Telegram Business account.
- **Fields**:
  - **remove_keyboard**: Boolean (Required: True)
    - Requests clients to remove the custom keyboard (user will not be able to summon this keyboard; if you want to hide the keyboard from sight but keep it accessible, use one_time_keyboard in ReplyKeyboardMarkup)
  - **selective**: Boolean (Required: False)
    - Optional. Use this parameter if you want to remove the keyboard for specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply to a message in the same chat and forum topic, sender of the original message. Example: A user votes in a poll, bot returns confirmation message in reply to the vote and removes the keyboard for that user, while still showing the keyboard with poll options to users who haven't voted yet.

💡 --- 💡

### 📦 InlineKeyboardMarkup <a id='inlinekeyboardmarkup'></a>
- **URL**: [https://core.telegram.org/bots/api#inlinekeyboardmarkup](https://core.telegram.org/bots/api#inlinekeyboardmarkup)
- **Description**:
  - This object represents an inline keyboard that appears right next to the message it belongs to.
- **Fields**:
  - **inline_keyboard**: Array of Array of InlineKeyboardButton (Required: True)
    - Array of button rows, each represented by an Array of InlineKeyboardButton objects

💡 --- 💡

### 📦 InlineKeyboardButton <a id='inlinekeyboardbutton'></a>
- **URL**: [https://core.telegram.org/bots/api#inlinekeyboardbutton](https://core.telegram.org/bots/api#inlinekeyboardbutton)
- **Description**:
  - This object represents one button of an inline keyboard. Exactly one of the optional fields must be used to specify type of the button.
- **Fields**:
  - **text**: String (Required: True)
    - Label text on the button
  - **url**: String (Required: False)
    - Optional. HTTP or tg:// URL to be opened when the button is pressed. Links tg://user?id=<user_id> can be used to mention a user by their identifier without using a username, if this is allowed by their privacy settings.
  - **callback_data**: String (Required: False)
    - Optional. Data to be sent in a callback query to the bot when the button is pressed, 1-64 bytes
  - **web_app**: WebAppInfo (Required: False)
    - Optional. Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method answerWebAppQuery. Available only in private chats between a user and the bot. Not supported for messages sent on behalf of a Telegram Business account.
  - **login_url**: LoginUrl (Required: False)
    - Optional. An HTTPS URL used to automatically authorize the user. Can be used as a replacement for the Telegram Login Widget.
  - **switch_inline_query**: String (Required: False)
    - Optional. If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field. May be empty, in which case just the bot's username will be inserted. Not supported for messages sent on behalf of a Telegram Business account.
  - **switch_inline_query_current_chat**: String (Required: False)
    - Optional. If set, pressing the button will insert the bot's username and the specified inline query in the current chat's input field. May be empty, in which case only the bot's username will be inserted. This offers a quick way for the user to open your bot in inline mode in the same chat - good for selecting something from multiple options. Not supported in channels and for messages sent on behalf of a Telegram Business account.
  - **switch_inline_query_chosen_chat**: SwitchInlineQueryChosenChat (Required: False)
    - Optional. If set, pressing the button will prompt the user to select one of their chats of the specified type, open that chat and insert the bot's username and the specified inline query in the input field. Not supported for messages sent on behalf of a Telegram Business account.
  - **callback_game**: CallbackGame (Required: False)
    - Optional. Description of the game that will be launched when the user presses the button. NOTE: This type of button must always be the first button in the first row.
  - **pay**: Boolean (Required: False)
    - Optional. Specify True, to send a Pay button. Substrings "⭐" and "XTR" in the buttons's text will be replaced with a Telegram Star icon. NOTE: This type of button must always be the first button in the first row and can only be used in invoice messages.

💡 --- 💡

### 📦 LoginUrl <a id='loginurl'></a>
- **URL**: [https://core.telegram.org/bots/api#loginurl](https://core.telegram.org/bots/api#loginurl)
- **Description**:
  - This object represents a parameter of the inline keyboard button used to automatically authorize a user. Serves as a great replacement for the Telegram Login Widget when the user is coming from Telegram. All the user needs to do is tap/click a button and confirm that they want to log in:
  - Telegram apps support these buttons as of version 5.7.
- **Fields**:
  - **url**: String (Required: True)
    - An HTTPS URL to be opened with user authorization data added to the query string when the button is pressed. If the user refuses to provide authorization data, the original URL without information about the user will be opened. The data added is the same as described in Receiving authorization data. NOTE: You must always check the hash of the received data to verify the authentication and the integrity of the data as described in Checking authorization.
  - **forward_text**: String (Required: False)
    - Optional. New text of the button in forwarded messages.
  - **bot_username**: String (Required: False)
    - Optional. Username of a bot, which will be used for user authorization. See Setting up a bot for more details. If not specified, the current bot's username will be assumed. The url's domain must be the same as the domain linked with the bot. See Linking your domain to the bot for more details.
  - **request_write_access**: Boolean (Required: False)
    - Optional. Pass True to request the permission for your bot to send messages to the user.

💡 --- 💡

### 📦 SwitchInlineQueryChosenChat <a id='switchinlinequerychosenchat'></a>
- **URL**: [https://core.telegram.org/bots/api#switchinlinequerychosenchat](https://core.telegram.org/bots/api#switchinlinequerychosenchat)
- **Description**:
  - This object represents an inline button that switches the current user to inline mode in a chosen chat, with an optional default inline query.
- **Fields**:
  - **query**: String (Required: False)
    - Optional. The default inline query to be inserted in the input field. If left empty, only the bot's username will be inserted
  - **allow_user_chats**: Boolean (Required: False)
    - Optional. True, if private chats with users can be chosen
  - **allow_bot_chats**: Boolean (Required: False)
    - Optional. True, if private chats with bots can be chosen
  - **allow_group_chats**: Boolean (Required: False)
    - Optional. True, if group and supergroup chats can be chosen
  - **allow_channel_chats**: Boolean (Required: False)
    - Optional. True, if channel chats can be chosen

💡 --- 💡

### 📦 CallbackQuery <a id='callbackquery'></a>
- **URL**: [https://core.telegram.org/bots/api#callbackquery](https://core.telegram.org/bots/api#callbackquery)
- **Description**:
  - This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present.
- **Fields**:
  - **id**: String (Required: True)
    - Unique identifier for this query
  - **from**: User (Required: True)
    - Sender
  - **message**: MaybeInaccessibleMessage (Required: False)
    - Optional. Message sent by the bot with the callback button that originated the query
  - **inline_message_id**: String (Required: False)
    - Optional. Identifier of the message sent via the bot in inline mode, that originated the query.
  - **chat_instance**: String (Required: True)
    - Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games.
  - **data**: String (Required: False)
    - Optional. Data associated with the callback button. Be aware that the message originated the query can contain no callback buttons with this data.
  - **game_short_name**: String (Required: False)
    - Optional. Short name of a Game to be returned, serves as the unique identifier for the game

💡 --- 💡

### 📦 ForceReply <a id='forcereply'></a>
- **URL**: [https://core.telegram.org/bots/api#forcereply](https://core.telegram.org/bots/api#forcereply)
- **Description**:
  - Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode. Not supported in channels and for messages sent on behalf of a Telegram Business account.
- **Fields**:
  - **force_reply**: Boolean (Required: True)
    - Shows reply interface to the user, as if they manually selected the bot's message and tapped 'Reply'
  - **input_field_placeholder**: String (Required: False)
    - Optional. The placeholder to be shown in the input field when the reply is active; 1-64 characters
  - **selective**: Boolean (Required: False)
    - Optional. Use this parameter if you want to force reply from specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply to a message in the same chat and forum topic, sender of the original message.

💡 --- 💡

### 📦 ChatPhoto <a id='chatphoto'></a>
- **URL**: [https://core.telegram.org/bots/api#chatphoto](https://core.telegram.org/bots/api#chatphoto)
- **Description**:
  - This object represents a chat photo.
- **Fields**:
  - **small_file_id**: String (Required: True)
    - File identifier of small (160x160) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.
  - **small_file_unique_id**: String (Required: True)
    - Unique file identifier of small (160x160) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
  - **big_file_id**: String (Required: True)
    - File identifier of big (640x640) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.
  - **big_file_unique_id**: String (Required: True)
    - Unique file identifier of big (640x640) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.

💡 --- 💡

### 📦 ChatInviteLink <a id='chatinvitelink'></a>
- **URL**: [https://core.telegram.org/bots/api#chatinvitelink](https://core.telegram.org/bots/api#chatinvitelink)
- **Description**:
  - Represents an invite link for a chat.
- **Fields**:
  - **invite_link**: String (Required: True)
    - The invite link. If the link was created by another chat administrator, then the second part of the link will be replaced with "...".
  - **creator**: User (Required: True)
    - Creator of the link
  - **creates_join_request**: Boolean (Required: True)
    - True, if users joining the chat via the link need to be approved by chat administrators
  - **is_primary**: Boolean (Required: True)
    - True, if the link is primary
  - **is_revoked**: Boolean (Required: True)
    - True, if the link is revoked
  - **name**: String (Required: False)
    - Optional. Invite link name
  - **expire_date**: Integer (Required: False)
    - Optional. Point in time (Unix timestamp) when the link will expire or has been expired
  - **member_limit**: Integer (Required: False)
    - Optional. The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999
  - **pending_join_request_count**: Integer (Required: False)
    - Optional. Number of pending join requests created using this link
  - **subscription_period**: Integer (Required: False)
    - Optional. The number of seconds the subscription will be active for before the next payment
  - **subscription_price**: Integer (Required: False)
    - Optional. The amount of Telegram Stars a user must pay initially and after each subsequent subscription period to be a member of the chat using the link

💡 --- 💡

### 📦 ChatAdministratorRights <a id='chatadministratorrights'></a>
- **URL**: [https://core.telegram.org/bots/api#chatadministratorrights](https://core.telegram.org/bots/api#chatadministratorrights)
- **Description**:
  - Represents the rights of an administrator in a chat.
- **Fields**:
  - **is_anonymous**: Boolean (Required: True)
    - True, if the user's presence in the chat is hidden
  - **can_manage_chat**: Boolean (Required: True)
    - True, if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages and ignore slow mode. Implied by any other administrator privilege.
  - **can_delete_messages**: Boolean (Required: True)
    - True, if the administrator can delete messages of other users
  - **can_manage_video_chats**: Boolean (Required: True)
    - True, if the administrator can manage video chats
  - **can_restrict_members**: Boolean (Required: True)
    - True, if the administrator can restrict, ban or unban chat members, or access supergroup statistics
  - **can_promote_members**: Boolean (Required: True)
    - True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by the user)
  - **can_change_info**: Boolean (Required: True)
    - True, if the user is allowed to change the chat title, photo and other settings
  - **can_invite_users**: Boolean (Required: True)
    - True, if the user is allowed to invite new users to the chat
  - **can_post_stories**: Boolean (Required: True)
    - True, if the administrator can post stories to the chat
  - **can_edit_stories**: Boolean (Required: True)
    - True, if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat's story archive
  - **can_delete_stories**: Boolean (Required: True)
    - True, if the administrator can delete stories posted by other users
  - **can_post_messages**: Boolean (Required: False)
    - Optional. True, if the administrator can post messages in the channel, or access channel statistics; for channels only
  - **can_edit_messages**: Boolean (Required: False)
    - Optional. True, if the administrator can edit messages of other users and can pin messages; for channels only
  - **can_pin_messages**: Boolean (Required: False)
    - Optional. True, if the user is allowed to pin messages; for groups and supergroups only
  - **can_manage_topics**: Boolean (Required: False)
    - Optional. True, if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only

💡 --- 💡

### 📦 ChatMemberUpdated <a id='chatmemberupdated'></a>
- **URL**: [https://core.telegram.org/bots/api#chatmemberupdated](https://core.telegram.org/bots/api#chatmemberupdated)
- **Description**:
  - This object represents changes in the status of a chat member.
- **Fields**:
  - **chat**: Chat (Required: True)
    - Chat the user belongs to
  - **from**: User (Required: True)
    - Performer of the action, which resulted in the change
  - **date**: Integer (Required: True)
    - Date the change was done in Unix time
  - **old_chat_member**: ChatMember (Required: True)
    - Previous information about the chat member
  - **new_chat_member**: ChatMember (Required: True)
    - New information about the chat member
  - **invite_link**: ChatInviteLink (Required: False)
    - Optional. Chat invite link, which was used by the user to join the chat; for joining by invite link events only.
  - **via_join_request**: Boolean (Required: False)
    - Optional. True, if the user joined the chat after sending a direct join request without using an invite link and being approved by an administrator
  - **via_chat_folder_invite_link**: Boolean (Required: False)
    - Optional. True, if the user joined the chat via a chat folder invite link

💡 --- 💡

### 📦 ChatMember <a id='chatmember'></a>
- **URL**: [https://core.telegram.org/bots/api#chatmember](https://core.telegram.org/bots/api#chatmember)
- **Description**:
  - This object contains information about one member of a chat. Currently, the following 6 types of chat members are supported:
  - - ChatMemberOwner
  - - ChatMemberAdministrator
  - - ChatMemberMember
  - - ChatMemberRestricted
  - - ChatMemberLeft
  - - ChatMemberBanned
- **Subtypes**:
  - ChatMemberOwner
  - ChatMemberAdministrator
  - ChatMemberMember
  - ChatMemberRestricted
  - ChatMemberLeft
  - ChatMemberBanned

💡 --- 💡

### 📦 ChatMemberOwner <a id='chatmemberowner'></a>
- **URL**: [https://core.telegram.org/bots/api#chatmemberowner](https://core.telegram.org/bots/api#chatmemberowner)
- **Description**:
  - Represents a chat member that owns the chat and has all administrator privileges.
- **Fields**:
  - **status**: String (Required: True)
    - The member's status in the chat, always "creator"
  - **user**: User (Required: True)
    - Information about the user
  - **is_anonymous**: Boolean (Required: True)
    - True, if the user's presence in the chat is hidden
  - **custom_title**: String (Required: False)
    - Optional. Custom title for this user

💡 --- 💡

### 📦 ChatMemberAdministrator <a id='chatmemberadministrator'></a>
- **URL**: [https://core.telegram.org/bots/api#chatmemberadministrator](https://core.telegram.org/bots/api#chatmemberadministrator)
- **Description**:
  - Represents a chat member that has some additional privileges.
- **Fields**:
  - **status**: String (Required: True)
    - The member's status in the chat, always "administrator"
  - **user**: User (Required: True)
    - Information about the user
  - **can_be_edited**: Boolean (Required: True)
    - True, if the bot is allowed to edit administrator privileges of that user
  - **is_anonymous**: Boolean (Required: True)
    - True, if the user's presence in the chat is hidden
  - **can_manage_chat**: Boolean (Required: True)
    - True, if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages and ignore slow mode. Implied by any other administrator privilege.
  - **can_delete_messages**: Boolean (Required: True)
    - True, if the administrator can delete messages of other users
  - **can_manage_video_chats**: Boolean (Required: True)
    - True, if the administrator can manage video chats
  - **can_restrict_members**: Boolean (Required: True)
    - True, if the administrator can restrict, ban or unban chat members, or access supergroup statistics
  - **can_promote_members**: Boolean (Required: True)
    - True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by the user)
  - **can_change_info**: Boolean (Required: True)
    - True, if the user is allowed to change the chat title, photo and other settings
  - **can_invite_users**: Boolean (Required: True)
    - True, if the user is allowed to invite new users to the chat
  - **can_post_stories**: Boolean (Required: True)
    - True, if the administrator can post stories to the chat
  - **can_edit_stories**: Boolean (Required: True)
    - True, if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat's story archive
  - **can_delete_stories**: Boolean (Required: True)
    - True, if the administrator can delete stories posted by other users
  - **can_post_messages**: Boolean (Required: False)
    - Optional. True, if the administrator can post messages in the channel, or access channel statistics; for channels only
  - **can_edit_messages**: Boolean (Required: False)
    - Optional. True, if the administrator can edit messages of other users and can pin messages; for channels only
  - **can_pin_messages**: Boolean (Required: False)
    - Optional. True, if the user is allowed to pin messages; for groups and supergroups only
  - **can_manage_topics**: Boolean (Required: False)
    - Optional. True, if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only
  - **custom_title**: String (Required: False)
    - Optional. Custom title for this user

💡 --- 💡

### 📦 ChatMemberMember <a id='chatmembermember'></a>
- **URL**: [https://core.telegram.org/bots/api#chatmembermember](https://core.telegram.org/bots/api#chatmembermember)
- **Description**:
  - Represents a chat member that has no additional privileges or restrictions.
- **Fields**:
  - **status**: String (Required: True)
    - The member's status in the chat, always "member"
  - **user**: User (Required: True)
    - Information about the user
  - **until_date**: Integer (Required: False)
    - Optional. Date when the user's subscription will expire; Unix time

💡 --- 💡

### 📦 ChatMemberRestricted <a id='chatmemberrestricted'></a>
- **URL**: [https://core.telegram.org/bots/api#chatmemberrestricted](https://core.telegram.org/bots/api#chatmemberrestricted)
- **Description**:
  - Represents a chat member that is under certain restrictions in the chat. Supergroups only.
- **Fields**:
  - **status**: String (Required: True)
    - The member's status in the chat, always "restricted"
  - **user**: User (Required: True)
    - Information about the user
  - **is_member**: Boolean (Required: True)
    - True, if the user is a member of the chat at the moment of the request
  - **can_send_messages**: Boolean (Required: True)
    - True, if the user is allowed to send text messages, contacts, giveaways, giveaway winners, invoices, locations and venues
  - **can_send_audios**: Boolean (Required: True)
    - True, if the user is allowed to send audios
  - **can_send_documents**: Boolean (Required: True)
    - True, if the user is allowed to send documents
  - **can_send_photos**: Boolean (Required: True)
    - True, if the user is allowed to send photos
  - **can_send_videos**: Boolean (Required: True)
    - True, if the user is allowed to send videos
  - **can_send_video_notes**: Boolean (Required: True)
    - True, if the user is allowed to send video notes
  - **can_send_voice_notes**: Boolean (Required: True)
    - True, if the user is allowed to send voice notes
  - **can_send_polls**: Boolean (Required: True)
    - True, if the user is allowed to send polls
  - **can_send_other_messages**: Boolean (Required: True)
    - True, if the user is allowed to send animations, games, stickers and use inline bots
  - **can_add_web_page_previews**: Boolean (Required: True)
    - True, if the user is allowed to add web page previews to their messages
  - **can_change_info**: Boolean (Required: True)
    - True, if the user is allowed to change the chat title, photo and other settings
  - **can_invite_users**: Boolean (Required: True)
    - True, if the user is allowed to invite new users to the chat
  - **can_pin_messages**: Boolean (Required: True)
    - True, if the user is allowed to pin messages
  - **can_manage_topics**: Boolean (Required: True)
    - True, if the user is allowed to create forum topics
  - **until_date**: Integer (Required: True)
    - Date when restrictions will be lifted for this user; Unix time. If 0, then the user is restricted forever

💡 --- 💡

### 📦 ChatMemberLeft <a id='chatmemberleft'></a>
- **URL**: [https://core.telegram.org/bots/api#chatmemberleft](https://core.telegram.org/bots/api#chatmemberleft)
- **Description**:
  - Represents a chat member that isn't currently a member of the chat, but may join it themselves.
- **Fields**:
  - **status**: String (Required: True)
    - The member's status in the chat, always "left"
  - **user**: User (Required: True)
    - Information about the user

💡 --- 💡

### 📦 ChatMemberBanned <a id='chatmemberbanned'></a>
- **URL**: [https://core.telegram.org/bots/api#chatmemberbanned](https://core.telegram.org/bots/api#chatmemberbanned)
- **Description**:
  - Represents a chat member that was banned in the chat and can't return to the chat or view chat messages.
- **Fields**:
  - **status**: String (Required: True)
    - The member's status in the chat, always "kicked"
  - **user**: User (Required: True)
    - Information about the user
  - **until_date**: Integer (Required: True)
    - Date when restrictions will be lifted for this user; Unix time. If 0, then the user is banned forever

💡 --- 💡

### 📦 ChatJoinRequest <a id='chatjoinrequest'></a>
- **URL**: [https://core.telegram.org/bots/api#chatjoinrequest](https://core.telegram.org/bots/api#chatjoinrequest)
- **Description**:
  - Represents a join request sent to a chat.
- **Fields**:
  - **chat**: Chat (Required: True)
    - Chat to which the request was sent
  - **from**: User (Required: True)
    - User that sent the join request
  - **user_chat_id**: Integer (Required: True)
    - Identifier of a private chat with the user who sent the join request. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot can use this identifier for 5 minutes to send messages until the join request is processed, assuming no other administrator contacted the user.
  - **date**: Integer (Required: True)
    - Date the request was sent in Unix time
  - **bio**: String (Required: False)
    - Optional. Bio of the user.
  - **invite_link**: ChatInviteLink (Required: False)
    - Optional. Chat invite link that was used by the user to send the join request

💡 --- 💡

### 📦 ChatPermissions <a id='chatpermissions'></a>
- **URL**: [https://core.telegram.org/bots/api#chatpermissions](https://core.telegram.org/bots/api#chatpermissions)
- **Description**:
  - Describes actions that a non-administrator user is allowed to take in a chat.
- **Fields**:
  - **can_send_messages**: Boolean (Required: False)
    - Optional. True, if the user is allowed to send text messages, contacts, giveaways, giveaway winners, invoices, locations and venues
  - **can_send_audios**: Boolean (Required: False)
    - Optional. True, if the user is allowed to send audios
  - **can_send_documents**: Boolean (Required: False)
    - Optional. True, if the user is allowed to send documents
  - **can_send_photos**: Boolean (Required: False)
    - Optional. True, if the user is allowed to send photos
  - **can_send_videos**: Boolean (Required: False)
    - Optional. True, if the user is allowed to send videos
  - **can_send_video_notes**: Boolean (Required: False)
    - Optional. True, if the user is allowed to send video notes
  - **can_send_voice_notes**: Boolean (Required: False)
    - Optional. True, if the user is allowed to send voice notes
  - **can_send_polls**: Boolean (Required: False)
    - Optional. True, if the user is allowed to send polls
  - **can_send_other_messages**: Boolean (Required: False)
    - Optional. True, if the user is allowed to send animations, games, stickers and use inline bots
  - **can_add_web_page_previews**: Boolean (Required: False)
    - Optional. True, if the user is allowed to add web page previews to their messages
  - **can_change_info**: Boolean (Required: False)
    - Optional. True, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups
  - **can_invite_users**: Boolean (Required: False)
    - Optional. True, if the user is allowed to invite new users to the chat
  - **can_pin_messages**: Boolean (Required: False)
    - Optional. True, if the user is allowed to pin messages. Ignored in public supergroups
  - **can_manage_topics**: Boolean (Required: False)
    - Optional. True, if the user is allowed to create forum topics. If omitted defaults to the value of can_pin_messages

💡 --- 💡

### 📦 Birthdate <a id='birthdate'></a>
- **URL**: [https://core.telegram.org/bots/api#birthdate](https://core.telegram.org/bots/api#birthdate)
- **Description**:
  - Describes the birthdate of a user.
- **Fields**:
  - **day**: Integer (Required: True)
    - Day of the user's birth; 1-31
  - **month**: Integer (Required: True)
    - Month of the user's birth; 1-12
  - **year**: Integer (Required: False)
    - Optional. Year of the user's birth

💡 --- 💡

### 📦 BusinessIntro <a id='businessintro'></a>
- **URL**: [https://core.telegram.org/bots/api#businessintro](https://core.telegram.org/bots/api#businessintro)
- **Description**:
  - Contains information about the start page settings of a Telegram Business account.
- **Fields**:
  - **title**: String (Required: False)
    - Optional. Title text of the business intro
  - **message**: String (Required: False)
    - Optional. Message text of the business intro
  - **sticker**: Sticker (Required: False)
    - Optional. Sticker of the business intro

💡 --- 💡

### 📦 BusinessLocation <a id='businesslocation'></a>
- **URL**: [https://core.telegram.org/bots/api#businesslocation](https://core.telegram.org/bots/api#businesslocation)
- **Description**:
  - Contains information about the location of a Telegram Business account.
- **Fields**:
  - **address**: String (Required: True)
    - Address of the business
  - **location**: Location (Required: False)
    - Optional. Location of the business

💡 --- 💡

### 📦 BusinessOpeningHoursInterval <a id='businessopeninghoursinterval'></a>
- **URL**: [https://core.telegram.org/bots/api#businessopeninghoursinterval](https://core.telegram.org/bots/api#businessopeninghoursinterval)
- **Description**:
  - Describes an interval of time during which a business is open.
- **Fields**:
  - **opening_minute**: Integer (Required: True)
    - The minute's sequence number in a week, starting on Monday, marking the start of the time interval during which the business is open; 0 - 7 * 24 * 60
  - **closing_minute**: Integer (Required: True)
    - The minute's sequence number in a week, starting on Monday, marking the end of the time interval during which the business is open; 0 - 8 * 24 * 60

💡 --- 💡

### 📦 BusinessOpeningHours <a id='businessopeninghours'></a>
- **URL**: [https://core.telegram.org/bots/api#businessopeninghours](https://core.telegram.org/bots/api#businessopeninghours)
- **Description**:
  - Describes the opening hours of a business.
- **Fields**:
  - **time_zone_name**: String (Required: True)
    - Unique name of the time zone for which the opening hours are defined
  - **opening_hours**: Array of BusinessOpeningHoursInterval (Required: True)
    - List of time intervals describing business opening hours

💡 --- 💡

### 📦 ChatLocation <a id='chatlocation'></a>
- **URL**: [https://core.telegram.org/bots/api#chatlocation](https://core.telegram.org/bots/api#chatlocation)
- **Description**:
  - Represents a location to which a chat is connected.
- **Fields**:
  - **location**: Location (Required: True)
    - The location to which the supergroup is connected. Can't be a live location.
  - **address**: String (Required: True)
    - Location address; 1-64 characters, as defined by the chat owner

💡 --- 💡

### 📦 ReactionType <a id='reactiontype'></a>
- **URL**: [https://core.telegram.org/bots/api#reactiontype](https://core.telegram.org/bots/api#reactiontype)
- **Description**:
  - This object describes the type of a reaction. Currently, it can be one of
  - - ReactionTypeEmoji
  - - ReactionTypeCustomEmoji
  - - ReactionTypePaid
- **Subtypes**:
  - ReactionTypeEmoji
  - ReactionTypeCustomEmoji
  - ReactionTypePaid

💡 --- 💡

### 📦 ReactionTypeEmoji <a id='reactiontypeemoji'></a>
- **URL**: [https://core.telegram.org/bots/api#reactiontypeemoji](https://core.telegram.org/bots/api#reactiontypeemoji)
- **Description**:
  - The reaction is based on an emoji.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the reaction, always "emoji"
  - **emoji**: String (Required: True)
    - Reaction emoji. Currently, it can be one of "👍", "👎", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", "🎉", "🤩", "🤮", "💩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴", "😍", "🐳", "❤‍🔥", "🌚", "🌭", "💯", "🤣", "⚡", "🍌", "🏆", "💔", "🤨", "😐", "🍓", "🍾", "💋", "🖕", "😈", "😴", "😭", "🤓", "👻", "👨‍💻", "👀", "🎃", "🙈", "😇", "😨", "🤝", "✍", "🤗", "🫡", "🎅", "🎄", "☃", "💅", "🤪", "🗿", "🆒", "💘", "🙉", "🦄", "😘", "💊", "🙊", "😎", "👾", "🤷‍♂", "🤷", "🤷‍♀", "😡"

💡 --- 💡

### 📦 ReactionTypeCustomEmoji <a id='reactiontypecustomemoji'></a>
- **URL**: [https://core.telegram.org/bots/api#reactiontypecustomemoji](https://core.telegram.org/bots/api#reactiontypecustomemoji)
- **Description**:
  - The reaction is based on a custom emoji.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the reaction, always "custom_emoji"
  - **custom_emoji_id**: String (Required: True)
    - Custom emoji identifier

💡 --- 💡

### 📦 ReactionTypePaid <a id='reactiontypepaid'></a>
- **URL**: [https://core.telegram.org/bots/api#reactiontypepaid](https://core.telegram.org/bots/api#reactiontypepaid)
- **Description**:
  - The reaction is paid.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the reaction, always "paid"

💡 --- 💡

### 📦 ReactionCount <a id='reactioncount'></a>
- **URL**: [https://core.telegram.org/bots/api#reactioncount](https://core.telegram.org/bots/api#reactioncount)
- **Description**:
  - Represents a reaction added to a message along with the number of times it was added.
- **Fields**:
  - **type**: ReactionType (Required: True)
    - Type of the reaction
  - **total_count**: Integer (Required: True)
    - Number of times the reaction was added

💡 --- 💡

### 📦 MessageReactionUpdated <a id='messagereactionupdated'></a>
- **URL**: [https://core.telegram.org/bots/api#messagereactionupdated](https://core.telegram.org/bots/api#messagereactionupdated)
- **Description**:
  - This object represents a change of a reaction on a message performed by a user.
- **Fields**:
  - **chat**: Chat (Required: True)
    - The chat containing the message the user reacted to
  - **message_id**: Integer (Required: True)
    - Unique identifier of the message inside the chat
  - **user**: User (Required: False)
    - Optional. The user that changed the reaction, if the user isn't anonymous
  - **actor_chat**: Chat (Required: False)
    - Optional. The chat on behalf of which the reaction was changed, if the user is anonymous
  - **date**: Integer (Required: True)
    - Date of the change in Unix time
  - **old_reaction**: Array of ReactionType (Required: True)
    - Previous list of reaction types that were set by the user
  - **new_reaction**: Array of ReactionType (Required: True)
    - New list of reaction types that have been set by the user

💡 --- 💡

### 📦 MessageReactionCountUpdated <a id='messagereactioncountupdated'></a>
- **URL**: [https://core.telegram.org/bots/api#messagereactioncountupdated](https://core.telegram.org/bots/api#messagereactioncountupdated)
- **Description**:
  - This object represents reaction changes on a message with anonymous reactions.
- **Fields**:
  - **chat**: Chat (Required: True)
    - The chat containing the message
  - **message_id**: Integer (Required: True)
    - Unique message identifier inside the chat
  - **date**: Integer (Required: True)
    - Date of the change in Unix time
  - **reactions**: Array of ReactionCount (Required: True)
    - List of reactions that are present on the message

💡 --- 💡

### 📦 ForumTopic <a id='forumtopic'></a>
- **URL**: [https://core.telegram.org/bots/api#forumtopic](https://core.telegram.org/bots/api#forumtopic)
- **Description**:
  - This object represents a forum topic.
- **Fields**:
  - **message_thread_id**: Integer (Required: True)
    - Unique identifier of the forum topic
  - **name**: String (Required: True)
    - Name of the topic
  - **icon_color**: Integer (Required: True)
    - Color of the topic icon in RGB format
  - **icon_custom_emoji_id**: String (Required: False)
    - Optional. Unique identifier of the custom emoji shown as the topic icon

💡 --- 💡

### 📦 BotCommand <a id='botcommand'></a>
- **URL**: [https://core.telegram.org/bots/api#botcommand](https://core.telegram.org/bots/api#botcommand)
- **Description**:
  - This object represents a bot command.
- **Fields**:
  - **command**: String (Required: True)
    - Text of the command; 1-32 characters. Can contain only lowercase English letters, digits and underscores.
  - **description**: String (Required: True)
    - Description of the command; 1-256 characters.

💡 --- 💡

### 📦 BotCommandScope <a id='botcommandscope'></a>
- **URL**: [https://core.telegram.org/bots/api#botcommandscope](https://core.telegram.org/bots/api#botcommandscope)
- **Description**:
  - This object represents the scope to which bot commands are applied. Currently, the following 7 scopes are supported:
  - - BotCommandScopeDefault
  - - BotCommandScopeAllPrivateChats
  - - BotCommandScopeAllGroupChats
  - - BotCommandScopeAllChatAdministrators
  - - BotCommandScopeChat
  - - BotCommandScopeChatAdministrators
  - - BotCommandScopeChatMember
- **Subtypes**:
  - BotCommandScopeDefault
  - BotCommandScopeAllPrivateChats
  - BotCommandScopeAllGroupChats
  - BotCommandScopeAllChatAdministrators
  - BotCommandScopeChat
  - BotCommandScopeChatAdministrators
  - BotCommandScopeChatMember

💡 --- 💡

### 📦 BotCommandScopeDefault <a id='botcommandscopedefault'></a>
- **URL**: [https://core.telegram.org/bots/api#botcommandscopedefault](https://core.telegram.org/bots/api#botcommandscopedefault)
- **Description**:
  - Represents the default scope of bot commands. Default commands are used if no commands with a narrower scope are specified for the user.
- **Fields**:
  - **type**: String (Required: True)
    - Scope type, must be default

💡 --- 💡

### 📦 BotCommandScopeAllPrivateChats <a id='botcommandscopeallprivatechats'></a>
- **URL**: [https://core.telegram.org/bots/api#botcommandscopeallprivatechats](https://core.telegram.org/bots/api#botcommandscopeallprivatechats)
- **Description**:
  - Represents the scope of bot commands, covering all private chats.
- **Fields**:
  - **type**: String (Required: True)
    - Scope type, must be all_private_chats

💡 --- 💡

### 📦 BotCommandScopeAllGroupChats <a id='botcommandscopeallgroupchats'></a>
- **URL**: [https://core.telegram.org/bots/api#botcommandscopeallgroupchats](https://core.telegram.org/bots/api#botcommandscopeallgroupchats)
- **Description**:
  - Represents the scope of bot commands, covering all group and supergroup chats.
- **Fields**:
  - **type**: String (Required: True)
    - Scope type, must be all_group_chats

💡 --- 💡

### 📦 BotCommandScopeAllChatAdministrators <a id='botcommandscopeallchatadministrators'></a>
- **URL**: [https://core.telegram.org/bots/api#botcommandscopeallchatadministrators](https://core.telegram.org/bots/api#botcommandscopeallchatadministrators)
- **Description**:
  - Represents the scope of bot commands, covering all group and supergroup chat administrators.
- **Fields**:
  - **type**: String (Required: True)
    - Scope type, must be all_chat_administrators

💡 --- 💡

### 📦 BotCommandScopeChat <a id='botcommandscopechat'></a>
- **URL**: [https://core.telegram.org/bots/api#botcommandscopechat](https://core.telegram.org/bots/api#botcommandscopechat)
- **Description**:
  - Represents the scope of bot commands, covering a specific chat.
- **Fields**:
  - **type**: String (Required: True)
    - Scope type, must be chat
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)

💡 --- 💡

### 📦 BotCommandScopeChatAdministrators <a id='botcommandscopechatadministrators'></a>
- **URL**: [https://core.telegram.org/bots/api#botcommandscopechatadministrators](https://core.telegram.org/bots/api#botcommandscopechatadministrators)
- **Description**:
  - Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat.
- **Fields**:
  - **type**: String (Required: True)
    - Scope type, must be chat_administrators
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)

💡 --- 💡

### 📦 BotCommandScopeChatMember <a id='botcommandscopechatmember'></a>
- **URL**: [https://core.telegram.org/bots/api#botcommandscopechatmember](https://core.telegram.org/bots/api#botcommandscopechatmember)
- **Description**:
  - Represents the scope of bot commands, covering a specific member of a group or supergroup chat.
- **Fields**:
  - **type**: String (Required: True)
    - Scope type, must be chat_member
  - **chat_id**: Integer, String (Required: True)
    - Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
  - **user_id**: Integer (Required: True)
    - Unique identifier of the target user

💡 --- 💡

### 📦 BotName <a id='botname'></a>
- **URL**: [https://core.telegram.org/bots/api#botname](https://core.telegram.org/bots/api#botname)
- **Description**:
  - This object represents the bot's name.
- **Fields**:
  - **name**: String (Required: True)
    - The bot's name

💡 --- 💡

### 📦 BotDescription <a id='botdescription'></a>
- **URL**: [https://core.telegram.org/bots/api#botdescription](https://core.telegram.org/bots/api#botdescription)
- **Description**:
  - This object represents the bot's description.
- **Fields**:
  - **description**: String (Required: True)
    - The bot's description

💡 --- 💡

### 📦 BotShortDescription <a id='botshortdescription'></a>
- **URL**: [https://core.telegram.org/bots/api#botshortdescription](https://core.telegram.org/bots/api#botshortdescription)
- **Description**:
  - This object represents the bot's short description.
- **Fields**:
  - **short_description**: String (Required: True)
    - The bot's short description

💡 --- 💡

### 📦 MenuButton <a id='menubutton'></a>
- **URL**: [https://core.telegram.org/bots/api#menubutton](https://core.telegram.org/bots/api#menubutton)
- **Description**:
  - This object describes the bot's menu button in a private chat. It should be one of
  - - MenuButtonCommands
  - - MenuButtonWebApp
  - - MenuButtonDefault
  - If a menu button other than MenuButtonDefault is set for a private chat, then it is applied in the chat. Otherwise the default menu button is applied. By default, the menu button opens the list of bot commands.
- **Subtypes**:
  - MenuButtonCommands
  - MenuButtonWebApp
  - MenuButtonDefault

💡 --- 💡

### 📦 MenuButtonCommands <a id='menubuttoncommands'></a>
- **URL**: [https://core.telegram.org/bots/api#menubuttoncommands](https://core.telegram.org/bots/api#menubuttoncommands)
- **Description**:
  - Represents a menu button, which opens the bot's list of commands.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the button, must be commands

💡 --- 💡

### 📦 MenuButtonWebApp <a id='menubuttonwebapp'></a>
- **URL**: [https://core.telegram.org/bots/api#menubuttonwebapp](https://core.telegram.org/bots/api#menubuttonwebapp)
- **Description**:
  - Represents a menu button, which launches a Web App.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the button, must be web_app
  - **text**: String (Required: True)
    - Text on the button
  - **web_app**: WebAppInfo (Required: True)
    - Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method answerWebAppQuery. Alternatively, a t.me link to a Web App of the bot can be specified in the object instead of the Web App's URL, in which case the Web App will be opened as if the user pressed the link.

💡 --- 💡

### 📦 MenuButtonDefault <a id='menubuttondefault'></a>
- **URL**: [https://core.telegram.org/bots/api#menubuttondefault](https://core.telegram.org/bots/api#menubuttondefault)
- **Description**:
  - Describes that no specific value for the menu button was set.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the button, must be default

💡 --- 💡

### 📦 ChatBoostSource <a id='chatboostsource'></a>
- **URL**: [https://core.telegram.org/bots/api#chatboostsource](https://core.telegram.org/bots/api#chatboostsource)
- **Description**:
  - This object describes the source of a chat boost. It can be one of
  - - ChatBoostSourcePremium
  - - ChatBoostSourceGiftCode
  - - ChatBoostSourceGiveaway
- **Subtypes**:
  - ChatBoostSourcePremium
  - ChatBoostSourceGiftCode
  - ChatBoostSourceGiveaway

💡 --- 💡

### 📦 ChatBoostSourcePremium <a id='chatboostsourcepremium'></a>
- **URL**: [https://core.telegram.org/bots/api#chatboostsourcepremium](https://core.telegram.org/bots/api#chatboostsourcepremium)
- **Description**:
  - The boost was obtained by subscribing to Telegram Premium or by gifting a Telegram Premium subscription to another user.
- **Fields**:
  - **source**: String (Required: True)
    - Source of the boost, always "premium"
  - **user**: User (Required: True)
    - User that boosted the chat

💡 --- 💡

### 📦 ChatBoostSourceGiftCode <a id='chatboostsourcegiftcode'></a>
- **URL**: [https://core.telegram.org/bots/api#chatboostsourcegiftcode](https://core.telegram.org/bots/api#chatboostsourcegiftcode)
- **Description**:
  - The boost was obtained by the creation of Telegram Premium gift codes to boost a chat. Each such code boosts the chat 4 times for the duration of the corresponding Telegram Premium subscription.
- **Fields**:
  - **source**: String (Required: True)
    - Source of the boost, always "gift_code"
  - **user**: User (Required: True)
    - User for which the gift code was created

💡 --- 💡

### 📦 ChatBoostSourceGiveaway <a id='chatboostsourcegiveaway'></a>
- **URL**: [https://core.telegram.org/bots/api#chatboostsourcegiveaway](https://core.telegram.org/bots/api#chatboostsourcegiveaway)
- **Description**:
  - The boost was obtained by the creation of a Telegram Premium or a Telegram Star giveaway. This boosts the chat 4 times for the duration of the corresponding Telegram Premium subscription for Telegram Premium giveaways and prize_star_count / 500 times for one year for Telegram Star giveaways.
- **Fields**:
  - **source**: String (Required: True)
    - Source of the boost, always "giveaway"
  - **giveaway_message_id**: Integer (Required: True)
    - Identifier of a message in the chat with the giveaway; the message could have been deleted already. May be 0 if the message isn't sent yet.
  - **user**: User (Required: False)
    - Optional. User that won the prize in the giveaway if any; for Telegram Premium giveaways only
  - **prize_star_count**: Integer (Required: False)
    - Optional. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only
  - **is_unclaimed**: Boolean (Required: False)
    - Optional. True, if the giveaway was completed, but there was no user to win the prize

💡 --- 💡

### 📦 ChatBoost <a id='chatboost'></a>
- **URL**: [https://core.telegram.org/bots/api#chatboost](https://core.telegram.org/bots/api#chatboost)
- **Description**:
  - This object contains information about a chat boost.
- **Fields**:
  - **boost_id**: String (Required: True)
    - Unique identifier of the boost
  - **add_date**: Integer (Required: True)
    - Point in time (Unix timestamp) when the chat was boosted
  - **expiration_date**: Integer (Required: True)
    - Point in time (Unix timestamp) when the boost will automatically expire, unless the booster's Telegram Premium subscription is prolonged
  - **source**: ChatBoostSource (Required: True)
    - Source of the added boost

💡 --- 💡

### 📦 ChatBoostUpdated <a id='chatboostupdated'></a>
- **URL**: [https://core.telegram.org/bots/api#chatboostupdated](https://core.telegram.org/bots/api#chatboostupdated)
- **Description**:
  - This object represents a boost added to a chat or changed.
- **Fields**:
  - **chat**: Chat (Required: True)
    - Chat which was boosted
  - **boost**: ChatBoost (Required: True)
    - Information about the chat boost

💡 --- 💡

### 📦 ChatBoostRemoved <a id='chatboostremoved'></a>
- **URL**: [https://core.telegram.org/bots/api#chatboostremoved](https://core.telegram.org/bots/api#chatboostremoved)
- **Description**:
  - This object represents a boost removed from a chat.
- **Fields**:
  - **chat**: Chat (Required: True)
    - Chat which was boosted
  - **boost_id**: String (Required: True)
    - Unique identifier of the boost
  - **remove_date**: Integer (Required: True)
    - Point in time (Unix timestamp) when the boost was removed
  - **source**: ChatBoostSource (Required: True)
    - Source of the removed boost

💡 --- 💡

### 📦 UserChatBoosts <a id='userchatboosts'></a>
- **URL**: [https://core.telegram.org/bots/api#userchatboosts](https://core.telegram.org/bots/api#userchatboosts)
- **Description**:
  - This object represents a list of boosts added to a chat by a user.
- **Fields**:
  - **boosts**: Array of ChatBoost (Required: True)
    - The list of boosts added to the chat by the user

💡 --- 💡

### 📦 BusinessConnection <a id='businessconnection'></a>
- **URL**: [https://core.telegram.org/bots/api#businessconnection](https://core.telegram.org/bots/api#businessconnection)
- **Description**:
  - Describes the connection of the bot with a business account.
- **Fields**:
  - **id**: String (Required: True)
    - Unique identifier of the business connection
  - **user**: User (Required: True)
    - Business account user that created the business connection
  - **user_chat_id**: Integer (Required: True)
    - Identifier of a private chat with the user who created the business connection. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
  - **date**: Integer (Required: True)
    - Date the connection was established in Unix time
  - **can_reply**: Boolean (Required: True)
    - True, if the bot can act on behalf of the business account in chats that were active in the last 24 hours
  - **is_enabled**: Boolean (Required: True)
    - True, if the connection is active

💡 --- 💡

### 📦 BusinessMessagesDeleted <a id='businessmessagesdeleted'></a>
- **URL**: [https://core.telegram.org/bots/api#businessmessagesdeleted](https://core.telegram.org/bots/api#businessmessagesdeleted)
- **Description**:
  - This object is received when messages are deleted from a connected business account.
- **Fields**:
  - **business_connection_id**: String (Required: True)
    - Unique identifier of the business connection
  - **chat**: Chat (Required: True)
    - Information about a chat in the business account. The bot may not have access to the chat or the corresponding user.
  - **message_ids**: Array of Integer (Required: True)
    - The list of identifiers of deleted messages in the chat of the business account

💡 --- 💡

### 📦 ResponseParameters <a id='responseparameters'></a>
- **URL**: [https://core.telegram.org/bots/api#responseparameters](https://core.telegram.org/bots/api#responseparameters)
- **Description**:
  - Describes why a request was unsuccessful.
- **Fields**:
  - **migrate_to_chat_id**: Integer (Required: False)
    - Optional. The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
  - **retry_after**: Integer (Required: False)
    - Optional. In case of exceeding flood control, the number of seconds left to wait before the request can be repeated

💡 --- 💡

### 📦 InputMedia <a id='inputmedia'></a>
- **URL**: [https://core.telegram.org/bots/api#inputmedia](https://core.telegram.org/bots/api#inputmedia)
- **Description**:
  - This object represents the content of a media message to be sent. It should be one of
  - - InputMediaAnimation
  - - InputMediaDocument
  - - InputMediaAudio
  - - InputMediaPhoto
  - - InputMediaVideo
- **Subtypes**:
  - InputMediaAnimation
  - InputMediaDocument
  - InputMediaAudio
  - InputMediaPhoto
  - InputMediaVideo

💡 --- 💡

### 📦 InputMediaPhoto <a id='inputmediaphoto'></a>
- **URL**: [https://core.telegram.org/bots/api#inputmediaphoto](https://core.telegram.org/bots/api#inputmediaphoto)
- **Description**:
  - Represents a photo to be sent.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the result, must be photo
  - **media**: String (Required: True)
    - File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
  - **caption**: String (Required: False)
    - Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
  - **show_caption_above_media**: Boolean (Required: False)
    - Optional. Pass True, if the caption must be shown above the message media
  - **has_spoiler**: Boolean (Required: False)
    - Optional. Pass True if the photo needs to be covered with a spoiler animation

💡 --- 💡

### 📦 InputMediaVideo <a id='inputmediavideo'></a>
- **URL**: [https://core.telegram.org/bots/api#inputmediavideo](https://core.telegram.org/bots/api#inputmediavideo)
- **Description**:
  - Represents a video to be sent.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the result, must be video
  - **media**: String (Required: True)
    - File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
  - **thumbnail**: InputFile, String (Required: False)
    - Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
  - **caption**: String (Required: False)
    - Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Optional. Mode for parsing entities in the video caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
  - **show_caption_above_media**: Boolean (Required: False)
    - Optional. Pass True, if the caption must be shown above the message media
  - **width**: Integer (Required: False)
    - Optional. Video width
  - **height**: Integer (Required: False)
    - Optional. Video height
  - **duration**: Integer (Required: False)
    - Optional. Video duration in seconds
  - **supports_streaming**: Boolean (Required: False)
    - Optional. Pass True if the uploaded video is suitable for streaming
  - **has_spoiler**: Boolean (Required: False)
    - Optional. Pass True if the video needs to be covered with a spoiler animation

💡 --- 💡

### 📦 InputMediaAnimation <a id='inputmediaanimation'></a>
- **URL**: [https://core.telegram.org/bots/api#inputmediaanimation](https://core.telegram.org/bots/api#inputmediaanimation)
- **Description**:
  - Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the result, must be animation
  - **media**: String (Required: True)
    - File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
  - **thumbnail**: InputFile, String (Required: False)
    - Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
  - **caption**: String (Required: False)
    - Optional. Caption of the animation to be sent, 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Optional. Mode for parsing entities in the animation caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
  - **show_caption_above_media**: Boolean (Required: False)
    - Optional. Pass True, if the caption must be shown above the message media
  - **width**: Integer (Required: False)
    - Optional. Animation width
  - **height**: Integer (Required: False)
    - Optional. Animation height
  - **duration**: Integer (Required: False)
    - Optional. Animation duration in seconds
  - **has_spoiler**: Boolean (Required: False)
    - Optional. Pass True if the animation needs to be covered with a spoiler animation

💡 --- 💡

### 📦 InputMediaAudio <a id='inputmediaaudio'></a>
- **URL**: [https://core.telegram.org/bots/api#inputmediaaudio](https://core.telegram.org/bots/api#inputmediaaudio)
- **Description**:
  - Represents an audio file to be treated as music to be sent.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the result, must be audio
  - **media**: String (Required: True)
    - File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
  - **thumbnail**: InputFile, String (Required: False)
    - Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
  - **caption**: String (Required: False)
    - Optional. Caption of the audio to be sent, 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Optional. Mode for parsing entities in the audio caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
  - **duration**: Integer (Required: False)
    - Optional. Duration of the audio in seconds
  - **performer**: String (Required: False)
    - Optional. Performer of the audio
  - **title**: String (Required: False)
    - Optional. Title of the audio

💡 --- 💡

### 📦 InputMediaDocument <a id='inputmediadocument'></a>
- **URL**: [https://core.telegram.org/bots/api#inputmediadocument](https://core.telegram.org/bots/api#inputmediadocument)
- **Description**:
  - Represents a general file to be sent.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the result, must be document
  - **media**: String (Required: True)
    - File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
  - **thumbnail**: InputFile, String (Required: False)
    - Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
  - **caption**: String (Required: False)
    - Optional. Caption of the document to be sent, 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Optional. Mode for parsing entities in the document caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
  - **disable_content_type_detection**: Boolean (Required: False)
    - Optional. Disables automatic server-side content type detection for files uploaded using multipart/form-data. Always True, if the document is sent as part of an album.

💡 --- 💡

### 📦 InputFile <a id='inputfile'></a>
- **URL**: [https://core.telegram.org/bots/api#inputfile](https://core.telegram.org/bots/api#inputfile)
- **Description**:
  - This object represents the contents of a file to be uploaded. Must be posted using multipart/form-data in the usual way that files are uploaded via the browser.

💡 --- 💡

### 📦 InputPaidMedia <a id='inputpaidmedia'></a>
- **URL**: [https://core.telegram.org/bots/api#inputpaidmedia](https://core.telegram.org/bots/api#inputpaidmedia)
- **Description**:
  - This object describes the paid media to be sent. Currently, it can be one of
  - - InputPaidMediaPhoto
  - - InputPaidMediaVideo
- **Subtypes**:
  - InputPaidMediaPhoto
  - InputPaidMediaVideo

💡 --- 💡

### 📦 InputPaidMediaPhoto <a id='inputpaidmediaphoto'></a>
- **URL**: [https://core.telegram.org/bots/api#inputpaidmediaphoto](https://core.telegram.org/bots/api#inputpaidmediaphoto)
- **Description**:
  - The paid media to send is a photo.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the media, must be photo
  - **media**: String (Required: True)
    - File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files: https://core.telegram.org/bots/api#sending-files

💡 --- 💡

### 📦 InputPaidMediaVideo <a id='inputpaidmediavideo'></a>
- **URL**: [https://core.telegram.org/bots/api#inputpaidmediavideo](https://core.telegram.org/bots/api#inputpaidmediavideo)
- **Description**:
  - The paid media to send is a video.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the media, must be video
  - **media**: String (Required: True)
    - File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
  - **thumbnail**: InputFile, String (Required: False)
    - Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
  - **width**: Integer (Required: False)
    - Optional. Video width
  - **height**: Integer (Required: False)
    - Optional. Video height
  - **duration**: Integer (Required: False)
    - Optional. Video duration in seconds
  - **supports_streaming**: Boolean (Required: False)
    - Optional. Pass True if the uploaded video is suitable for streaming

💡 --- 💡

### 📦 Sticker <a id='sticker'></a>
- **URL**: [https://core.telegram.org/bots/api#sticker](https://core.telegram.org/bots/api#sticker)
- **Description**:
  - This object represents a sticker.
- **Fields**:
  - **file_id**: String (Required: True)
    - Identifier for this file, which can be used to download or reuse the file
  - **file_unique_id**: String (Required: True)
    - Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
  - **type**: String (Required: True)
    - Type of the sticker, currently one of "regular", "mask", "custom_emoji". The type of the sticker is independent from its format, which is determined by the fields is_animated and is_video.
  - **width**: Integer (Required: True)
    - Sticker width
  - **height**: Integer (Required: True)
    - Sticker height
  - **is_animated**: Boolean (Required: True)
    - True, if the sticker is animated
  - **is_video**: Boolean (Required: True)
    - True, if the sticker is a video sticker
  - **thumbnail**: PhotoSize (Required: False)
    - Optional. Sticker thumbnail in the .WEBP or .JPG format
  - **emoji**: String (Required: False)
    - Optional. Emoji associated with the sticker
  - **set_name**: String (Required: False)
    - Optional. Name of the sticker set to which the sticker belongs
  - **premium_animation**: File (Required: False)
    - Optional. For premium regular stickers, premium animation for the sticker
  - **mask_position**: MaskPosition (Required: False)
    - Optional. For mask stickers, the position where the mask should be placed
  - **custom_emoji_id**: String (Required: False)
    - Optional. For custom emoji stickers, unique identifier of the custom emoji
  - **needs_repainting**: Boolean (Required: False)
    - Optional. True, if the sticker must be repainted to a text color in messages, the color of the Telegram Premium badge in emoji status, white color on chat photos, or another appropriate color in other places
  - **file_size**: Integer (Required: False)
    - Optional. File size in bytes

💡 --- 💡

### 📦 StickerSet <a id='stickerset'></a>
- **URL**: [https://core.telegram.org/bots/api#stickerset](https://core.telegram.org/bots/api#stickerset)
- **Description**:
  - This object represents a sticker set.
- **Fields**:
  - **name**: String (Required: True)
    - Sticker set name
  - **title**: String (Required: True)
    - Sticker set title
  - **sticker_type**: String (Required: True)
    - Type of stickers in the set, currently one of "regular", "mask", "custom_emoji"
  - **stickers**: Array of Sticker (Required: True)
    - List of all set stickers
  - **thumbnail**: PhotoSize (Required: False)
    - Optional. Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format

💡 --- 💡

### 📦 MaskPosition <a id='maskposition'></a>
- **URL**: [https://core.telegram.org/bots/api#maskposition](https://core.telegram.org/bots/api#maskposition)
- **Description**:
  - This object describes the position on faces where a mask should be placed by default.
- **Fields**:
  - **point**: String (Required: True)
    - The part of the face relative to which the mask should be placed. One of "forehead", "eyes", "mouth", or "chin".
  - **x_shift**: Float (Required: True)
    - Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. For example, choosing -1.0 will place mask just to the left of the default mask position.
  - **y_shift**: Float (Required: True)
    - Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. For example, 1.0 will place the mask just below the default mask position.
  - **scale**: Float (Required: True)
    - Mask scaling coefficient. For example, 2.0 means double size.

💡 --- 💡

### 📦 InputSticker <a id='inputsticker'></a>
- **URL**: [https://core.telegram.org/bots/api#inputsticker](https://core.telegram.org/bots/api#inputsticker)
- **Description**:
  - This object describes a sticker to be added to a sticker set.
- **Fields**:
  - **sticker**: InputFile, String (Required: True)
    - The added sticker. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, upload a new one using multipart/form-data, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. Animated and video stickers can't be uploaded via HTTP URL. More information on Sending Files: https://core.telegram.org/bots/api#sending-files
  - **format**: String (Required: True)
    - Format of the added sticker, must be one of "static" for a .WEBP or .PNG image, "animated" for a .TGS animation, "video" for a WEBM video
  - **emoji_list**: Array of String (Required: True)
    - List of 1-20 emoji associated with the sticker
  - **mask_position**: MaskPosition (Required: False)
    - Optional. Position where the mask should be placed on faces. For "mask" stickers only.
  - **keywords**: Array of String (Required: False)
    - Optional. List of 0-20 search keywords for the sticker with total length of up to 64 characters. For "regular" and "custom_emoji" stickers only.

💡 --- 💡

### 📦 InlineQuery <a id='inlinequery'></a>
- **URL**: [https://core.telegram.org/bots/api#inlinequery](https://core.telegram.org/bots/api#inlinequery)
- **Description**:
  - This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.
- **Fields**:
  - **id**: String (Required: True)
    - Unique identifier for this query
  - **from**: User (Required: True)
    - Sender
  - **query**: String (Required: True)
    - Text of the query (up to 256 characters)
  - **offset**: String (Required: True)
    - Offset of the results to be returned, can be controlled by the bot
  - **chat_type**: String (Required: False)
    - Optional. Type of the chat from which the inline query was sent. Can be either "sender" for a private chat with the inline query sender, "private", "group", "supergroup", or "channel". The chat type should be always known for requests sent from official clients and most third-party clients, unless the request was sent from a secret chat
  - **location**: Location (Required: False)
    - Optional. Sender location, only for bots that request user location

💡 --- 💡

### 📦 InlineQueryResultsButton <a id='inlinequeryresultsbutton'></a>
- **URL**: [https://core.telegram.org/bots/api#inlinequeryresultsbutton](https://core.telegram.org/bots/api#inlinequeryresultsbutton)
- **Description**:
  - This object represents a button to be shown above inline query results. You must use exactly one of the optional fields.
- **Fields**:
  - **text**: String (Required: True)
    - Label text on the button
  - **web_app**: WebAppInfo (Required: False)
    - Optional. Description of the Web App that will be launched when the user presses the button. The Web App will be able to switch back to the inline mode using the method switchInlineQuery inside the Web App.
  - **start_parameter**: String (Required: False)
    - Optional. Deep-linking parameter for the /start message sent to the bot when a user presses the button. 1-64 characters, only A-Z, a-z, 0-9, _ and - are allowed. Example: An inline bot that sends YouTube videos can ask the user to connect the bot to their YouTube account to adapt search results accordingly. To do this, it displays a 'Connect your YouTube account' button above the results, or even before showing any. The user presses the button, switches to a private chat with the bot and, in doing so, passes a start parameter that instructs the bot to return an OAuth link. Once done, the bot can offer a switch_inline button so that the user can easily return to the chat where they wanted to use the bot's inline capabilities.

💡 --- 💡

### 📦 InlineQueryResult <a id='inlinequeryresult'></a>
- **URL**: [https://core.telegram.org/bots/api#inlinequeryresult](https://core.telegram.org/bots/api#inlinequeryresult)
- **Description**:
  - This object represents one result of an inline query. Telegram clients currently support results of the following 20 types:
  - - InlineQueryResultCachedAudio
  - - InlineQueryResultCachedDocument
  - - InlineQueryResultCachedGif
  - - InlineQueryResultCachedMpeg4Gif
  - - InlineQueryResultCachedPhoto
  - - InlineQueryResultCachedSticker
  - - InlineQueryResultCachedVideo
  - - InlineQueryResultCachedVoice
  - - InlineQueryResultArticle
  - - InlineQueryResultAudio
  - - InlineQueryResultContact
  - - InlineQueryResultGame
  - - InlineQueryResultDocument
  - - InlineQueryResultGif
  - - InlineQueryResultLocation
  - - InlineQueryResultMpeg4Gif
  - - InlineQueryResultPhoto
  - - InlineQueryResultVenue
  - - InlineQueryResultVideo
  - - InlineQueryResultVoice
  - Note: All URLs passed in inline query results will be available to end users and therefore must be assumed to be public.
- **Subtypes**:
  - InlineQueryResultCachedAudio
  - InlineQueryResultCachedDocument
  - InlineQueryResultCachedGif
  - InlineQueryResultCachedMpeg4Gif
  - InlineQueryResultCachedPhoto
  - InlineQueryResultCachedSticker
  - InlineQueryResultCachedVideo
  - InlineQueryResultCachedVoice
  - InlineQueryResultArticle
  - InlineQueryResultAudio
  - InlineQueryResultContact
  - InlineQueryResultGame
  - InlineQueryResultDocument
  - InlineQueryResultGif
  - InlineQueryResultLocation
  - InlineQueryResultMpeg4Gif
  - InlineQueryResultPhoto
  - InlineQueryResultVenue
  - InlineQueryResultVideo
  - InlineQueryResultVoice

💡 --- 💡

### 📦 InlineQueryResultArticle <a id='inlinequeryresultarticle'></a>
- **URL**: [https://core.telegram.org/bots/api#inlinequeryresultarticle](https://core.telegram.org/bots/api#inlinequeryresultarticle)
- **Description**:
  - Represents a link to an article or web page.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the result, must be article
  - **id**: String (Required: True)
    - Unique identifier for this result, 1-64 Bytes
  - **title**: String (Required: True)
    - Title of the result
  - **input_message_content**: InputMessageContent (Required: True)
    - Content of the message to be sent
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - Optional. Inline keyboard attached to the message
  - **url**: String (Required: False)
    - Optional. URL of the result
  - **hide_url**: Boolean (Required: False)
    - Optional. Pass True if you don't want the URL to be shown in the message
  - **description**: String (Required: False)
    - Optional. Short description of the result
  - **thumbnail_url**: String (Required: False)
    - Optional. Url of the thumbnail for the result
  - **thumbnail_width**: Integer (Required: False)
    - Optional. Thumbnail width
  - **thumbnail_height**: Integer (Required: False)
    - Optional. Thumbnail height

💡 --- 💡

### 📦 InlineQueryResultPhoto <a id='inlinequeryresultphoto'></a>
- **URL**: [https://core.telegram.org/bots/api#inlinequeryresultphoto](https://core.telegram.org/bots/api#inlinequeryresultphoto)
- **Description**:
  - Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the result, must be photo
  - **id**: String (Required: True)
    - Unique identifier for this result, 1-64 bytes
  - **photo_url**: String (Required: True)
    - A valid URL of the photo. Photo must be in JPEG format. Photo size must not exceed 5MB
  - **thumbnail_url**: String (Required: True)
    - URL of the thumbnail for the photo
  - **photo_width**: Integer (Required: False)
    - Optional. Width of the photo
  - **photo_height**: Integer (Required: False)
    - Optional. Height of the photo
  - **title**: String (Required: False)
    - Optional. Title for the result
  - **description**: String (Required: False)
    - Optional. Short description of the result
  - **caption**: String (Required: False)
    - Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
  - **show_caption_above_media**: Boolean (Required: False)
    - Optional. Pass True, if the caption must be shown above the message media
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - Optional. Inline keyboard attached to the message
  - **input_message_content**: InputMessageContent (Required: False)
    - Optional. Content of the message to be sent instead of the photo

💡 --- 💡

### 📦 InlineQueryResultGif <a id='inlinequeryresultgif'></a>
- **URL**: [https://core.telegram.org/bots/api#inlinequeryresultgif](https://core.telegram.org/bots/api#inlinequeryresultgif)
- **Description**:
  - Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the result, must be gif
  - **id**: String (Required: True)
    - Unique identifier for this result, 1-64 bytes
  - **gif_url**: String (Required: True)
    - A valid URL for the GIF file. File size must not exceed 1MB
  - **gif_width**: Integer (Required: False)
    - Optional. Width of the GIF
  - **gif_height**: Integer (Required: False)
    - Optional. Height of the GIF
  - **gif_duration**: Integer (Required: False)
    - Optional. Duration of the GIF in seconds
  - **thumbnail_url**: String (Required: True)
    - URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result
  - **thumbnail_mime_type**: String (Required: False)
    - Optional. MIME type of the thumbnail, must be one of "image/jpeg", "image/gif", or "video/mp4". Defaults to "image/jpeg"
  - **title**: String (Required: False)
    - Optional. Title for the result
  - **caption**: String (Required: False)
    - Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Optional. Mode for parsing entities in the caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
  - **show_caption_above_media**: Boolean (Required: False)
    - Optional. Pass True, if the caption must be shown above the message media
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - Optional. Inline keyboard attached to the message
  - **input_message_content**: InputMessageContent (Required: False)
    - Optional. Content of the message to be sent instead of the GIF animation

💡 --- 💡

### 📦 InlineQueryResultMpeg4Gif <a id='inlinequeryresultmpeg4gif'></a>
- **URL**: [https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif](https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif)
- **Description**:
  - Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the result, must be mpeg4_gif
  - **id**: String (Required: True)
    - Unique identifier for this result, 1-64 bytes
  - **mpeg4_url**: String (Required: True)
    - A valid URL for the MPEG4 file. File size must not exceed 1MB
  - **mpeg4_width**: Integer (Required: False)
    - Optional. Video width
  - **mpeg4_height**: Integer (Required: False)
    - Optional. Video height
  - **mpeg4_duration**: Integer (Required: False)
    - Optional. Video duration in seconds
  - **thumbnail_url**: String (Required: True)
    - URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result
  - **thumbnail_mime_type**: String (Required: False)
    - Optional. MIME type of the thumbnail, must be one of "image/jpeg", "image/gif", or "video/mp4". Defaults to "image/jpeg"
  - **title**: String (Required: False)
    - Optional. Title for the result
  - **caption**: String (Required: False)
    - Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Optional. Mode for parsing entities in the caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
  - **show_caption_above_media**: Boolean (Required: False)
    - Optional. Pass True, if the caption must be shown above the message media
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - Optional. Inline keyboard attached to the message
  - **input_message_content**: InputMessageContent (Required: False)
    - Optional. Content of the message to be sent instead of the video animation

💡 --- 💡

### 📦 InlineQueryResultVideo <a id='inlinequeryresultvideo'></a>
- **URL**: [https://core.telegram.org/bots/api#inlinequeryresultvideo](https://core.telegram.org/bots/api#inlinequeryresultvideo)
- **Description**:
  - Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the result, must be video
  - **id**: String (Required: True)
    - Unique identifier for this result, 1-64 bytes
  - **video_url**: String (Required: True)
    - A valid URL for the embedded video player or video file
  - **mime_type**: String (Required: True)
    - MIME type of the content of the video URL, "text/html" or "video/mp4"
  - **thumbnail_url**: String (Required: True)
    - URL of the thumbnail (JPEG only) for the video
  - **title**: String (Required: True)
    - Title for the result
  - **caption**: String (Required: False)
    - Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Optional. Mode for parsing entities in the video caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
  - **show_caption_above_media**: Boolean (Required: False)
    - Optional. Pass True, if the caption must be shown above the message media
  - **video_width**: Integer (Required: False)
    - Optional. Video width
  - **video_height**: Integer (Required: False)
    - Optional. Video height
  - **video_duration**: Integer (Required: False)
    - Optional. Video duration in seconds
  - **description**: String (Required: False)
    - Optional. Short description of the result
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - Optional. Inline keyboard attached to the message
  - **input_message_content**: InputMessageContent (Required: False)
    - Optional. Content of the message to be sent instead of the video. This field is required if InlineQueryResultVideo is used to send an HTML-page as a result (e.g., a YouTube video).

💡 --- 💡

### 📦 InlineQueryResultAudio <a id='inlinequeryresultaudio'></a>
- **URL**: [https://core.telegram.org/bots/api#inlinequeryresultaudio](https://core.telegram.org/bots/api#inlinequeryresultaudio)
- **Description**:
  - Represents a link to an MP3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the result, must be audio
  - **id**: String (Required: True)
    - Unique identifier for this result, 1-64 bytes
  - **audio_url**: String (Required: True)
    - A valid URL for the audio file
  - **title**: String (Required: True)
    - Title
  - **caption**: String (Required: False)
    - Optional. Caption, 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Optional. Mode for parsing entities in the audio caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
  - **performer**: String (Required: False)
    - Optional. Performer
  - **audio_duration**: Integer (Required: False)
    - Optional. Audio duration in seconds
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - Optional. Inline keyboard attached to the message
  - **input_message_content**: InputMessageContent (Required: False)
    - Optional. Content of the message to be sent instead of the audio

💡 --- 💡

### 📦 InlineQueryResultVoice <a id='inlinequeryresultvoice'></a>
- **URL**: [https://core.telegram.org/bots/api#inlinequeryresultvoice](https://core.telegram.org/bots/api#inlinequeryresultvoice)
- **Description**:
  - Represents a link to a voice recording in an .OGG container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the result, must be voice
  - **id**: String (Required: True)
    - Unique identifier for this result, 1-64 bytes
  - **voice_url**: String (Required: True)
    - A valid URL for the voice recording
  - **title**: String (Required: True)
    - Recording title
  - **caption**: String (Required: False)
    - Optional. Caption, 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Optional. Mode for parsing entities in the voice message caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
  - **voice_duration**: Integer (Required: False)
    - Optional. Recording duration in seconds
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - Optional. Inline keyboard attached to the message
  - **input_message_content**: InputMessageContent (Required: False)
    - Optional. Content of the message to be sent instead of the voice recording

💡 --- 💡

### 📦 InlineQueryResultDocument <a id='inlinequeryresultdocument'></a>
- **URL**: [https://core.telegram.org/bots/api#inlinequeryresultdocument](https://core.telegram.org/bots/api#inlinequeryresultdocument)
- **Description**:
  - Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the result, must be document
  - **id**: String (Required: True)
    - Unique identifier for this result, 1-64 bytes
  - **title**: String (Required: True)
    - Title for the result
  - **caption**: String (Required: False)
    - Optional. Caption of the document to be sent, 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Optional. Mode for parsing entities in the document caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
  - **document_url**: String (Required: True)
    - A valid URL for the file
  - **mime_type**: String (Required: True)
    - MIME type of the content of the file, either "application/pdf" or "application/zip"
  - **description**: String (Required: False)
    - Optional. Short description of the result
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - Optional. Inline keyboard attached to the message
  - **input_message_content**: InputMessageContent (Required: False)
    - Optional. Content of the message to be sent instead of the file
  - **thumbnail_url**: String (Required: False)
    - Optional. URL of the thumbnail (JPEG only) for the file
  - **thumbnail_width**: Integer (Required: False)
    - Optional. Thumbnail width
  - **thumbnail_height**: Integer (Required: False)
    - Optional. Thumbnail height

💡 --- 💡

### 📦 InlineQueryResultLocation <a id='inlinequeryresultlocation'></a>
- **URL**: [https://core.telegram.org/bots/api#inlinequeryresultlocation](https://core.telegram.org/bots/api#inlinequeryresultlocation)
- **Description**:
  - Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the result, must be location
  - **id**: String (Required: True)
    - Unique identifier for this result, 1-64 Bytes
  - **latitude**: Float (Required: True)
    - Location latitude in degrees
  - **longitude**: Float (Required: True)
    - Location longitude in degrees
  - **title**: String (Required: True)
    - Location title
  - **horizontal_accuracy**: Float (Required: False)
    - Optional. The radius of uncertainty for the location, measured in meters; 0-1500
  - **live_period**: Integer (Required: False)
    - Optional. Period in seconds during which the location can be updated, should be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely.
  - **heading**: Integer (Required: False)
    - Optional. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
  - **proximity_alert_radius**: Integer (Required: False)
    - Optional. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - Optional. Inline keyboard attached to the message
  - **input_message_content**: InputMessageContent (Required: False)
    - Optional. Content of the message to be sent instead of the location
  - **thumbnail_url**: String (Required: False)
    - Optional. Url of the thumbnail for the result
  - **thumbnail_width**: Integer (Required: False)
    - Optional. Thumbnail width
  - **thumbnail_height**: Integer (Required: False)
    - Optional. Thumbnail height

💡 --- 💡

### 📦 InlineQueryResultVenue <a id='inlinequeryresultvenue'></a>
- **URL**: [https://core.telegram.org/bots/api#inlinequeryresultvenue](https://core.telegram.org/bots/api#inlinequeryresultvenue)
- **Description**:
  - Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the result, must be venue
  - **id**: String (Required: True)
    - Unique identifier for this result, 1-64 Bytes
  - **latitude**: Float (Required: True)
    - Latitude of the venue location in degrees
  - **longitude**: Float (Required: True)
    - Longitude of the venue location in degrees
  - **title**: String (Required: True)
    - Title of the venue
  - **address**: String (Required: True)
    - Address of the venue
  - **foursquare_id**: String (Required: False)
    - Optional. Foursquare identifier of the venue if known
  - **foursquare_type**: String (Required: False)
    - Optional. Foursquare type of the venue, if known. (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".)
  - **google_place_id**: String (Required: False)
    - Optional. Google Places identifier of the venue
  - **google_place_type**: String (Required: False)
    - Optional. Google Places type of the venue. (See supported types.)
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - Optional. Inline keyboard attached to the message
  - **input_message_content**: InputMessageContent (Required: False)
    - Optional. Content of the message to be sent instead of the venue
  - **thumbnail_url**: String (Required: False)
    - Optional. Url of the thumbnail for the result
  - **thumbnail_width**: Integer (Required: False)
    - Optional. Thumbnail width
  - **thumbnail_height**: Integer (Required: False)
    - Optional. Thumbnail height

💡 --- 💡

### 📦 InlineQueryResultContact <a id='inlinequeryresultcontact'></a>
- **URL**: [https://core.telegram.org/bots/api#inlinequeryresultcontact](https://core.telegram.org/bots/api#inlinequeryresultcontact)
- **Description**:
  - Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the result, must be contact
  - **id**: String (Required: True)
    - Unique identifier for this result, 1-64 Bytes
  - **phone_number**: String (Required: True)
    - Contact's phone number
  - **first_name**: String (Required: True)
    - Contact's first name
  - **last_name**: String (Required: False)
    - Optional. Contact's last name
  - **vcard**: String (Required: False)
    - Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - Optional. Inline keyboard attached to the message
  - **input_message_content**: InputMessageContent (Required: False)
    - Optional. Content of the message to be sent instead of the contact
  - **thumbnail_url**: String (Required: False)
    - Optional. Url of the thumbnail for the result
  - **thumbnail_width**: Integer (Required: False)
    - Optional. Thumbnail width
  - **thumbnail_height**: Integer (Required: False)
    - Optional. Thumbnail height

💡 --- 💡

### 📦 InlineQueryResultGame <a id='inlinequeryresultgame'></a>
- **URL**: [https://core.telegram.org/bots/api#inlinequeryresultgame](https://core.telegram.org/bots/api#inlinequeryresultgame)
- **Description**:
  - Represents a Game.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the result, must be game
  - **id**: String (Required: True)
    - Unique identifier for this result, 1-64 bytes
  - **game_short_name**: String (Required: True)
    - Short name of the game
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - Optional. Inline keyboard attached to the message

💡 --- 💡

### 📦 InlineQueryResultCachedPhoto <a id='inlinequeryresultcachedphoto'></a>
- **URL**: [https://core.telegram.org/bots/api#inlinequeryresultcachedphoto](https://core.telegram.org/bots/api#inlinequeryresultcachedphoto)
- **Description**:
  - Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the result, must be photo
  - **id**: String (Required: True)
    - Unique identifier for this result, 1-64 bytes
  - **photo_file_id**: String (Required: True)
    - A valid file identifier of the photo
  - **title**: String (Required: False)
    - Optional. Title for the result
  - **description**: String (Required: False)
    - Optional. Short description of the result
  - **caption**: String (Required: False)
    - Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
  - **show_caption_above_media**: Boolean (Required: False)
    - Optional. Pass True, if the caption must be shown above the message media
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - Optional. Inline keyboard attached to the message
  - **input_message_content**: InputMessageContent (Required: False)
    - Optional. Content of the message to be sent instead of the photo

💡 --- 💡

### 📦 InlineQueryResultCachedGif <a id='inlinequeryresultcachedgif'></a>
- **URL**: [https://core.telegram.org/bots/api#inlinequeryresultcachedgif](https://core.telegram.org/bots/api#inlinequeryresultcachedgif)
- **Description**:
  - Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the result, must be gif
  - **id**: String (Required: True)
    - Unique identifier for this result, 1-64 bytes
  - **gif_file_id**: String (Required: True)
    - A valid file identifier for the GIF file
  - **title**: String (Required: False)
    - Optional. Title for the result
  - **caption**: String (Required: False)
    - Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Optional. Mode for parsing entities in the caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
  - **show_caption_above_media**: Boolean (Required: False)
    - Optional. Pass True, if the caption must be shown above the message media
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - Optional. Inline keyboard attached to the message
  - **input_message_content**: InputMessageContent (Required: False)
    - Optional. Content of the message to be sent instead of the GIF animation

💡 --- 💡

### 📦 InlineQueryResultCachedMpeg4Gif <a id='inlinequeryresultcachedmpeg4gif'></a>
- **URL**: [https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif](https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif)
- **Description**:
  - Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the result, must be mpeg4_gif
  - **id**: String (Required: True)
    - Unique identifier for this result, 1-64 bytes
  - **mpeg4_file_id**: String (Required: True)
    - A valid file identifier for the MPEG4 file
  - **title**: String (Required: False)
    - Optional. Title for the result
  - **caption**: String (Required: False)
    - Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Optional. Mode for parsing entities in the caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
  - **show_caption_above_media**: Boolean (Required: False)
    - Optional. Pass True, if the caption must be shown above the message media
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - Optional. Inline keyboard attached to the message
  - **input_message_content**: InputMessageContent (Required: False)
    - Optional. Content of the message to be sent instead of the video animation

💡 --- 💡

### 📦 InlineQueryResultCachedSticker <a id='inlinequeryresultcachedsticker'></a>
- **URL**: [https://core.telegram.org/bots/api#inlinequeryresultcachedsticker](https://core.telegram.org/bots/api#inlinequeryresultcachedsticker)
- **Description**:
  - Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the result, must be sticker
  - **id**: String (Required: True)
    - Unique identifier for this result, 1-64 bytes
  - **sticker_file_id**: String (Required: True)
    - A valid file identifier of the sticker
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - Optional. Inline keyboard attached to the message
  - **input_message_content**: InputMessageContent (Required: False)
    - Optional. Content of the message to be sent instead of the sticker

💡 --- 💡

### 📦 InlineQueryResultCachedDocument <a id='inlinequeryresultcacheddocument'></a>
- **URL**: [https://core.telegram.org/bots/api#inlinequeryresultcacheddocument](https://core.telegram.org/bots/api#inlinequeryresultcacheddocument)
- **Description**:
  - Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the result, must be document
  - **id**: String (Required: True)
    - Unique identifier for this result, 1-64 bytes
  - **title**: String (Required: True)
    - Title for the result
  - **document_file_id**: String (Required: True)
    - A valid file identifier for the file
  - **description**: String (Required: False)
    - Optional. Short description of the result
  - **caption**: String (Required: False)
    - Optional. Caption of the document to be sent, 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Optional. Mode for parsing entities in the document caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - Optional. Inline keyboard attached to the message
  - **input_message_content**: InputMessageContent (Required: False)
    - Optional. Content of the message to be sent instead of the file

💡 --- 💡

### 📦 InlineQueryResultCachedVideo <a id='inlinequeryresultcachedvideo'></a>
- **URL**: [https://core.telegram.org/bots/api#inlinequeryresultcachedvideo](https://core.telegram.org/bots/api#inlinequeryresultcachedvideo)
- **Description**:
  - Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the result, must be video
  - **id**: String (Required: True)
    - Unique identifier for this result, 1-64 bytes
  - **video_file_id**: String (Required: True)
    - A valid file identifier for the video file
  - **title**: String (Required: True)
    - Title for the result
  - **description**: String (Required: False)
    - Optional. Short description of the result
  - **caption**: String (Required: False)
    - Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Optional. Mode for parsing entities in the video caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
  - **show_caption_above_media**: Boolean (Required: False)
    - Optional. Pass True, if the caption must be shown above the message media
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - Optional. Inline keyboard attached to the message
  - **input_message_content**: InputMessageContent (Required: False)
    - Optional. Content of the message to be sent instead of the video

💡 --- 💡

### 📦 InlineQueryResultCachedVoice <a id='inlinequeryresultcachedvoice'></a>
- **URL**: [https://core.telegram.org/bots/api#inlinequeryresultcachedvoice](https://core.telegram.org/bots/api#inlinequeryresultcachedvoice)
- **Description**:
  - Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the voice message.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the result, must be voice
  - **id**: String (Required: True)
    - Unique identifier for this result, 1-64 bytes
  - **voice_file_id**: String (Required: True)
    - A valid file identifier for the voice message
  - **title**: String (Required: True)
    - Voice message title
  - **caption**: String (Required: False)
    - Optional. Caption, 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Optional. Mode for parsing entities in the voice message caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - Optional. Inline keyboard attached to the message
  - **input_message_content**: InputMessageContent (Required: False)
    - Optional. Content of the message to be sent instead of the voice message

💡 --- 💡

### 📦 InlineQueryResultCachedAudio <a id='inlinequeryresultcachedaudio'></a>
- **URL**: [https://core.telegram.org/bots/api#inlinequeryresultcachedaudio](https://core.telegram.org/bots/api#inlinequeryresultcachedaudio)
- **Description**:
  - Represents a link to an MP3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the result, must be audio
  - **id**: String (Required: True)
    - Unique identifier for this result, 1-64 bytes
  - **audio_file_id**: String (Required: True)
    - A valid file identifier for the audio file
  - **caption**: String (Required: False)
    - Optional. Caption, 0-1024 characters after entities parsing
  - **parse_mode**: String (Required: False)
    - Optional. Mode for parsing entities in the audio caption. See formatting options for more details.
  - **caption_entities**: Array of MessageEntity (Required: False)
    - Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
  - **reply_markup**: InlineKeyboardMarkup (Required: False)
    - Optional. Inline keyboard attached to the message
  - **input_message_content**: InputMessageContent (Required: False)
    - Optional. Content of the message to be sent instead of the audio

💡 --- 💡

### 📦 InputMessageContent <a id='inputmessagecontent'></a>
- **URL**: [https://core.telegram.org/bots/api#inputmessagecontent](https://core.telegram.org/bots/api#inputmessagecontent)
- **Description**:
  - This object represents the content of a message to be sent as a result of an inline query. Telegram clients currently support the following 5 types:
  - - InputTextMessageContent
  - - InputLocationMessageContent
  - - InputVenueMessageContent
  - - InputContactMessageContent
  - - InputInvoiceMessageContent
- **Subtypes**:
  - InputTextMessageContent
  - InputLocationMessageContent
  - InputVenueMessageContent
  - InputContactMessageContent
  - InputInvoiceMessageContent

💡 --- 💡

### 📦 InputTextMessageContent <a id='inputtextmessagecontent'></a>
- **URL**: [https://core.telegram.org/bots/api#inputtextmessagecontent](https://core.telegram.org/bots/api#inputtextmessagecontent)
- **Description**:
  - Represents the content of a text message to be sent as the result of an inline query.
- **Fields**:
  - **message_text**: String (Required: True)
    - Text of the message to be sent, 1-4096 characters
  - **parse_mode**: String (Required: False)
    - Optional. Mode for parsing entities in the message text. See formatting options for more details.
  - **entities**: Array of MessageEntity (Required: False)
    - Optional. List of special entities that appear in message text, which can be specified instead of parse_mode
  - **link_preview_options**: LinkPreviewOptions (Required: False)
    - Optional. Link preview generation options for the message

💡 --- 💡

### 📦 InputLocationMessageContent <a id='inputlocationmessagecontent'></a>
- **URL**: [https://core.telegram.org/bots/api#inputlocationmessagecontent](https://core.telegram.org/bots/api#inputlocationmessagecontent)
- **Description**:
  - Represents the content of a location message to be sent as the result of an inline query.
- **Fields**:
  - **latitude**: Float (Required: True)
    - Latitude of the location in degrees
  - **longitude**: Float (Required: True)
    - Longitude of the location in degrees
  - **horizontal_accuracy**: Float (Required: False)
    - Optional. The radius of uncertainty for the location, measured in meters; 0-1500
  - **live_period**: Integer (Required: False)
    - Optional. Period in seconds during which the location can be updated, should be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely.
  - **heading**: Integer (Required: False)
    - Optional. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
  - **proximity_alert_radius**: Integer (Required: False)
    - Optional. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.

💡 --- 💡

### 📦 InputVenueMessageContent <a id='inputvenuemessagecontent'></a>
- **URL**: [https://core.telegram.org/bots/api#inputvenuemessagecontent](https://core.telegram.org/bots/api#inputvenuemessagecontent)
- **Description**:
  - Represents the content of a venue message to be sent as the result of an inline query.
- **Fields**:
  - **latitude**: Float (Required: True)
    - Latitude of the venue in degrees
  - **longitude**: Float (Required: True)
    - Longitude of the venue in degrees
  - **title**: String (Required: True)
    - Name of the venue
  - **address**: String (Required: True)
    - Address of the venue
  - **foursquare_id**: String (Required: False)
    - Optional. Foursquare identifier of the venue, if known
  - **foursquare_type**: String (Required: False)
    - Optional. Foursquare type of the venue, if known. (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".)
  - **google_place_id**: String (Required: False)
    - Optional. Google Places identifier of the venue
  - **google_place_type**: String (Required: False)
    - Optional. Google Places type of the venue. (See supported types.)

💡 --- 💡

### 📦 InputContactMessageContent <a id='inputcontactmessagecontent'></a>
- **URL**: [https://core.telegram.org/bots/api#inputcontactmessagecontent](https://core.telegram.org/bots/api#inputcontactmessagecontent)
- **Description**:
  - Represents the content of a contact message to be sent as the result of an inline query.
- **Fields**:
  - **phone_number**: String (Required: True)
    - Contact's phone number
  - **first_name**: String (Required: True)
    - Contact's first name
  - **last_name**: String (Required: False)
    - Optional. Contact's last name
  - **vcard**: String (Required: False)
    - Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes

💡 --- 💡

### 📦 InputInvoiceMessageContent <a id='inputinvoicemessagecontent'></a>
- **URL**: [https://core.telegram.org/bots/api#inputinvoicemessagecontent](https://core.telegram.org/bots/api#inputinvoicemessagecontent)
- **Description**:
  - Represents the content of an invoice message to be sent as the result of an inline query.
- **Fields**:
  - **title**: String (Required: True)
    - Product name, 1-32 characters
  - **description**: String (Required: True)
    - Product description, 1-255 characters
  - **payload**: String (Required: True)
    - Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use it for your internal processes.
  - **provider_token**: String (Required: False)
    - Optional. Payment provider token, obtained via @BotFather. Pass an empty string for payments in Telegram Stars.
  - **currency**: String (Required: True)
    - Three-letter ISO 4217 currency code, see more on currencies. Pass "XTR" for payments in Telegram Stars.
  - **prices**: Array of LabeledPrice (Required: True)
    - Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in Telegram Stars.
  - **max_tip_amount**: Integer (Required: False)
    - Optional. The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0. Not supported for payments in Telegram Stars.
  - **suggested_tip_amounts**: Array of Integer (Required: False)
    - Optional. A JSON-serialized array of suggested amounts of tip in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.
  - **provider_data**: String (Required: False)
    - Optional. A JSON-serialized object for data about the invoice, which will be shared with the payment provider. A detailed description of the required fields should be provided by the payment provider.
  - **photo_url**: String (Required: False)
    - Optional. URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service.
  - **photo_size**: Integer (Required: False)
    - Optional. Photo size in bytes
  - **photo_width**: Integer (Required: False)
    - Optional. Photo width
  - **photo_height**: Integer (Required: False)
    - Optional. Photo height
  - **need_name**: Boolean (Required: False)
    - Optional. Pass True if you require the user's full name to complete the order. Ignored for payments in Telegram Stars.
  - **need_phone_number**: Boolean (Required: False)
    - Optional. Pass True if you require the user's phone number to complete the order. Ignored for payments in Telegram Stars.
  - **need_email**: Boolean (Required: False)
    - Optional. Pass True if you require the user's email address to complete the order. Ignored for payments in Telegram Stars.
  - **need_shipping_address**: Boolean (Required: False)
    - Optional. Pass True if you require the user's shipping address to complete the order. Ignored for payments in Telegram Stars.
  - **send_phone_number_to_provider**: Boolean (Required: False)
    - Optional. Pass True if the user's phone number should be sent to the provider. Ignored for payments in Telegram Stars.
  - **send_email_to_provider**: Boolean (Required: False)
    - Optional. Pass True if the user's email address should be sent to the provider. Ignored for payments in Telegram Stars.
  - **is_flexible**: Boolean (Required: False)
    - Optional. Pass True if the final price depends on the shipping method. Ignored for payments in Telegram Stars.

💡 --- 💡

### 📦 ChosenInlineResult <a id='choseninlineresult'></a>
- **URL**: [https://core.telegram.org/bots/api#choseninlineresult](https://core.telegram.org/bots/api#choseninlineresult)
- **Description**:
  - Represents a result of an inline query that was chosen by the user and sent to their chat partner.
  - Note: It is necessary to enable inline feedback via @BotFather in order to receive these objects in updates.
- **Fields**:
  - **result_id**: String (Required: True)
    - The unique identifier for the result that was chosen
  - **from**: User (Required: True)
    - The user that chose the result
  - **location**: Location (Required: False)
    - Optional. Sender location, only for bots that require user location
  - **inline_message_id**: String (Required: False)
    - Optional. Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message. Will be also received in callback queries and can be used to edit the message.
  - **query**: String (Required: True)
    - The query that was used to obtain the result

💡 --- 💡

### 📦 SentWebAppMessage <a id='sentwebappmessage'></a>
- **URL**: [https://core.telegram.org/bots/api#sentwebappmessage](https://core.telegram.org/bots/api#sentwebappmessage)
- **Description**:
  - Describes an inline message sent by a Web App on behalf of a user.
- **Fields**:
  - **inline_message_id**: String (Required: False)
    - Optional. Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message.

💡 --- 💡

### 📦 LabeledPrice <a id='labeledprice'></a>
- **URL**: [https://core.telegram.org/bots/api#labeledprice](https://core.telegram.org/bots/api#labeledprice)
- **Description**:
  - This object represents a portion of the price for goods or services.
- **Fields**:
  - **label**: String (Required: True)
    - Portion label
  - **amount**: Integer (Required: True)
    - Price of the product in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).

💡 --- 💡

### 📦 Invoice <a id='invoice'></a>
- **URL**: [https://core.telegram.org/bots/api#invoice](https://core.telegram.org/bots/api#invoice)
- **Description**:
  - This object contains basic information about an invoice.
- **Fields**:
  - **title**: String (Required: True)
    - Product name
  - **description**: String (Required: True)
    - Product description
  - **start_parameter**: String (Required: True)
    - Unique bot deep-linking parameter that can be used to generate this invoice
  - **currency**: String (Required: True)
    - Three-letter ISO 4217 currency code, or "XTR" for payments in Telegram Stars
  - **total_amount**: Integer (Required: True)
    - Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).

💡 --- 💡

### 📦 ShippingAddress <a id='shippingaddress'></a>
- **URL**: [https://core.telegram.org/bots/api#shippingaddress](https://core.telegram.org/bots/api#shippingaddress)
- **Description**:
  - This object represents a shipping address.
- **Fields**:
  - **country_code**: String (Required: True)
    - Two-letter ISO 3166-1 alpha-2 country code
  - **state**: String (Required: True)
    - State, if applicable
  - **city**: String (Required: True)
    - City
  - **street_line1**: String (Required: True)
    - First line for the address
  - **street_line2**: String (Required: True)
    - Second line for the address
  - **post_code**: String (Required: True)
    - Address post code

💡 --- 💡

### 📦 OrderInfo <a id='orderinfo'></a>
- **URL**: [https://core.telegram.org/bots/api#orderinfo](https://core.telegram.org/bots/api#orderinfo)
- **Description**:
  - This object represents information about an order.
- **Fields**:
  - **name**: String (Required: False)
    - Optional. User name
  - **phone_number**: String (Required: False)
    - Optional. User's phone number
  - **email**: String (Required: False)
    - Optional. User email
  - **shipping_address**: ShippingAddress (Required: False)
    - Optional. User shipping address

💡 --- 💡

### 📦 ShippingOption <a id='shippingoption'></a>
- **URL**: [https://core.telegram.org/bots/api#shippingoption](https://core.telegram.org/bots/api#shippingoption)
- **Description**:
  - This object represents one shipping option.
- **Fields**:
  - **id**: String (Required: True)
    - Shipping option identifier
  - **title**: String (Required: True)
    - Option title
  - **prices**: Array of LabeledPrice (Required: True)
    - List of price portions

💡 --- 💡

### 📦 SuccessfulPayment <a id='successfulpayment'></a>
- **URL**: [https://core.telegram.org/bots/api#successfulpayment](https://core.telegram.org/bots/api#successfulpayment)
- **Description**:
  - This object contains basic information about a successful payment.
- **Fields**:
  - **currency**: String (Required: True)
    - Three-letter ISO 4217 currency code, or "XTR" for payments in Telegram Stars
  - **total_amount**: Integer (Required: True)
    - Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
  - **invoice_payload**: String (Required: True)
    - Bot-specified invoice payload
  - **shipping_option_id**: String (Required: False)
    - Optional. Identifier of the shipping option chosen by the user
  - **order_info**: OrderInfo (Required: False)
    - Optional. Order information provided by the user
  - **telegram_payment_charge_id**: String (Required: True)
    - Telegram payment identifier
  - **provider_payment_charge_id**: String (Required: True)
    - Provider payment identifier

💡 --- 💡

### 📦 RefundedPayment <a id='refundedpayment'></a>
- **URL**: [https://core.telegram.org/bots/api#refundedpayment](https://core.telegram.org/bots/api#refundedpayment)
- **Description**:
  - This object contains basic information about a refunded payment.
- **Fields**:
  - **currency**: String (Required: True)
    - Three-letter ISO 4217 currency code, or "XTR" for payments in Telegram Stars. Currently, always "XTR"
  - **total_amount**: Integer (Required: True)
    - Total refunded price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45, total_amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
  - **invoice_payload**: String (Required: True)
    - Bot-specified invoice payload
  - **telegram_payment_charge_id**: String (Required: True)
    - Telegram payment identifier
  - **provider_payment_charge_id**: String (Required: False)
    - Optional. Provider payment identifier

💡 --- 💡

### 📦 ShippingQuery <a id='shippingquery'></a>
- **URL**: [https://core.telegram.org/bots/api#shippingquery](https://core.telegram.org/bots/api#shippingquery)
- **Description**:
  - This object contains information about an incoming shipping query.
- **Fields**:
  - **id**: String (Required: True)
    - Unique query identifier
  - **from**: User (Required: True)
    - User who sent the query
  - **invoice_payload**: String (Required: True)
    - Bot-specified invoice payload
  - **shipping_address**: ShippingAddress (Required: True)
    - User specified shipping address

💡 --- 💡

### 📦 PreCheckoutQuery <a id='precheckoutquery'></a>
- **URL**: [https://core.telegram.org/bots/api#precheckoutquery](https://core.telegram.org/bots/api#precheckoutquery)
- **Description**:
  - This object contains information about an incoming pre-checkout query.
- **Fields**:
  - **id**: String (Required: True)
    - Unique query identifier
  - **from**: User (Required: True)
    - User who sent the query
  - **currency**: String (Required: True)
    - Three-letter ISO 4217 currency code, or "XTR" for payments in Telegram Stars
  - **total_amount**: Integer (Required: True)
    - Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
  - **invoice_payload**: String (Required: True)
    - Bot-specified invoice payload
  - **shipping_option_id**: String (Required: False)
    - Optional. Identifier of the shipping option chosen by the user
  - **order_info**: OrderInfo (Required: False)
    - Optional. Order information provided by the user

💡 --- 💡

### 📦 PaidMediaPurchased <a id='paidmediapurchased'></a>
- **URL**: [https://core.telegram.org/bots/api#paidmediapurchased](https://core.telegram.org/bots/api#paidmediapurchased)
- **Description**:
  - This object contains information about a paid media purchase.
- **Fields**:
  - **from**: User (Required: True)
    - User who purchased the media
  - **paid_media_payload**: String (Required: True)
    - Bot-specified paid media payload

💡 --- 💡

### 📦 RevenueWithdrawalState <a id='revenuewithdrawalstate'></a>
- **URL**: [https://core.telegram.org/bots/api#revenuewithdrawalstate](https://core.telegram.org/bots/api#revenuewithdrawalstate)
- **Description**:
  - This object describes the state of a revenue withdrawal operation. Currently, it can be one of
  - - RevenueWithdrawalStatePending
  - - RevenueWithdrawalStateSucceeded
  - - RevenueWithdrawalStateFailed
- **Subtypes**:
  - RevenueWithdrawalStatePending
  - RevenueWithdrawalStateSucceeded
  - RevenueWithdrawalStateFailed

💡 --- 💡

### 📦 RevenueWithdrawalStatePending <a id='revenuewithdrawalstatepending'></a>
- **URL**: [https://core.telegram.org/bots/api#revenuewithdrawalstatepending](https://core.telegram.org/bots/api#revenuewithdrawalstatepending)
- **Description**:
  - The withdrawal is in progress.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the state, always "pending"

💡 --- 💡

### 📦 RevenueWithdrawalStateSucceeded <a id='revenuewithdrawalstatesucceeded'></a>
- **URL**: [https://core.telegram.org/bots/api#revenuewithdrawalstatesucceeded](https://core.telegram.org/bots/api#revenuewithdrawalstatesucceeded)
- **Description**:
  - The withdrawal succeeded.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the state, always "succeeded"
  - **date**: Integer (Required: True)
    - Date the withdrawal was completed in Unix time
  - **url**: String (Required: True)
    - An HTTPS URL that can be used to see transaction details

💡 --- 💡

### 📦 RevenueWithdrawalStateFailed <a id='revenuewithdrawalstatefailed'></a>
- **URL**: [https://core.telegram.org/bots/api#revenuewithdrawalstatefailed](https://core.telegram.org/bots/api#revenuewithdrawalstatefailed)
- **Description**:
  - The withdrawal failed and the transaction was refunded.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the state, always "failed"

💡 --- 💡

### 📦 TransactionPartner <a id='transactionpartner'></a>
- **URL**: [https://core.telegram.org/bots/api#transactionpartner](https://core.telegram.org/bots/api#transactionpartner)
- **Description**:
  - This object describes the source of a transaction, or its recipient for outgoing transactions. Currently, it can be one of
  - - TransactionPartnerUser
  - - TransactionPartnerFragment
  - - TransactionPartnerTelegramAds
  - - TransactionPartnerOther
- **Subtypes**:
  - TransactionPartnerUser
  - TransactionPartnerFragment
  - TransactionPartnerTelegramAds
  - TransactionPartnerOther

💡 --- 💡

### 📦 TransactionPartnerUser <a id='transactionpartneruser'></a>
- **URL**: [https://core.telegram.org/bots/api#transactionpartneruser](https://core.telegram.org/bots/api#transactionpartneruser)
- **Description**:
  - Describes a transaction with a user.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the transaction partner, always "user"
  - **user**: User (Required: True)
    - Information about the user
  - **invoice_payload**: String (Required: False)
    - Optional. Bot-specified invoice payload
  - **paid_media**: Array of PaidMedia (Required: False)
    - Optional. Information about the paid media bought by the user
  - **paid_media_payload**: String (Required: False)
    - Optional. Bot-specified paid media payload

💡 --- 💡

### 📦 TransactionPartnerFragment <a id='transactionpartnerfragment'></a>
- **URL**: [https://core.telegram.org/bots/api#transactionpartnerfragment](https://core.telegram.org/bots/api#transactionpartnerfragment)
- **Description**:
  - Describes a withdrawal transaction with Fragment.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the transaction partner, always "fragment"
  - **withdrawal_state**: RevenueWithdrawalState (Required: False)
    - Optional. State of the transaction if the transaction is outgoing

💡 --- 💡

### 📦 TransactionPartnerTelegramAds <a id='transactionpartnertelegramads'></a>
- **URL**: [https://core.telegram.org/bots/api#transactionpartnertelegramads](https://core.telegram.org/bots/api#transactionpartnertelegramads)
- **Description**:
  - Describes a withdrawal transaction to the Telegram Ads platform.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the transaction partner, always "telegram_ads"

💡 --- 💡

### 📦 TransactionPartnerOther <a id='transactionpartnerother'></a>
- **URL**: [https://core.telegram.org/bots/api#transactionpartnerother](https://core.telegram.org/bots/api#transactionpartnerother)
- **Description**:
  - Describes a transaction with an unknown source or recipient.
- **Fields**:
  - **type**: String (Required: True)
    - Type of the transaction partner, always "other"

💡 --- 💡

### 📦 StarTransaction <a id='startransaction'></a>
- **URL**: [https://core.telegram.org/bots/api#startransaction](https://core.telegram.org/bots/api#startransaction)
- **Description**:
  - Describes a Telegram Star transaction.
- **Fields**:
  - **id**: String (Required: True)
    - Unique identifier of the transaction. Coincides with the identifer of the original transaction for refund transactions. Coincides with SuccessfulPayment.telegram_payment_charge_id for successful incoming payments from users.
  - **amount**: Integer (Required: True)
    - Number of Telegram Stars transferred by the transaction
  - **date**: Integer (Required: True)
    - Date the transaction was created in Unix time
  - **source**: TransactionPartner (Required: False)
    - Optional. Source of an incoming transaction (e.g., a user purchasing goods or services, Fragment refunding a failed withdrawal). Only for incoming transactions
  - **receiver**: TransactionPartner (Required: False)
    - Optional. Receiver of an outgoing transaction (e.g., a user for a purchase refund, Fragment for a withdrawal). Only for outgoing transactions

💡 --- 💡

### 📦 StarTransactions <a id='startransactions'></a>
- **URL**: [https://core.telegram.org/bots/api#startransactions](https://core.telegram.org/bots/api#startransactions)
- **Description**:
  - Contains a list of Telegram Star transactions.
- **Fields**:
  - **transactions**: Array of StarTransaction (Required: True)
    - The list of transactions

💡 --- 💡

### 📦 PassportData <a id='passportdata'></a>
- **URL**: [https://core.telegram.org/bots/api#passportdata](https://core.telegram.org/bots/api#passportdata)
- **Description**:
  - Describes Telegram Passport data shared with the bot by the user.
- **Fields**:
  - **data**: Array of EncryptedPassportElement (Required: True)
    - Array with information about documents and other Telegram Passport elements that was shared with the bot
  - **credentials**: EncryptedCredentials (Required: True)
    - Encrypted credentials required to decrypt the data

💡 --- 💡

### 📦 PassportFile <a id='passportfile'></a>
- **URL**: [https://core.telegram.org/bots/api#passportfile](https://core.telegram.org/bots/api#passportfile)
- **Description**:
  - This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB.
- **Fields**:
  - **file_id**: String (Required: True)
    - Identifier for this file, which can be used to download or reuse the file
  - **file_unique_id**: String (Required: True)
    - Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
  - **file_size**: Integer (Required: True)
    - File size in bytes
  - **file_date**: Integer (Required: True)
    - Unix time when the file was uploaded

💡 --- 💡

### 📦 EncryptedPassportElement <a id='encryptedpassportelement'></a>
- **URL**: [https://core.telegram.org/bots/api#encryptedpassportelement](https://core.telegram.org/bots/api#encryptedpassportelement)
- **Description**:
  - Describes documents or other Telegram Passport elements shared with the bot by the user.
- **Fields**:
  - **type**: String (Required: True)
    - Element type. One of "personal_details", "passport", "driver_license", "identity_card", "internal_passport", "address", "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration", "phone_number", "email".
  - **data**: String (Required: False)
    - Optional. Base64-encoded encrypted Telegram Passport element data provided by the user; available only for "personal_details", "passport", "driver_license", "identity_card", "internal_passport" and "address" types. Can be decrypted and verified using the accompanying EncryptedCredentials.
  - **phone_number**: String (Required: False)
    - Optional. User's verified phone number; available only for "phone_number" type
  - **email**: String (Required: False)
    - Optional. User's verified email address; available only for "email" type
  - **files**: Array of PassportFile (Required: False)
    - Optional. Array of encrypted files with documents provided by the user; available only for "utility_bill", "bank_statement", "rental_agreement", "passport_registration" and "temporary_registration" types. Files can be decrypted and verified using the accompanying EncryptedCredentials.
  - **front_side**: PassportFile (Required: False)
    - Optional. Encrypted file with the front side of the document, provided by the user; available only for "passport", "driver_license", "identity_card" and "internal_passport". The file can be decrypted and verified using the accompanying EncryptedCredentials.
  - **reverse_side**: PassportFile (Required: False)
    - Optional. Encrypted file with the reverse side of the document, provided by the user; available only for "driver_license" and "identity_card". The file can be decrypted and verified using the accompanying EncryptedCredentials.
  - **selfie**: PassportFile (Required: False)
    - Optional. Encrypted file with the selfie of the user holding a document, provided by the user; available if requested for "passport", "driver_license", "identity_card" and "internal_passport". The file can be decrypted and verified using the accompanying EncryptedCredentials.
  - **translation**: Array of PassportFile (Required: False)
    - Optional. Array of encrypted files with translated versions of documents provided by the user; available if requested for "passport", "driver_license", "identity_card", "internal_passport", "utility_bill", "bank_statement", "rental_agreement", "passport_registration" and "temporary_registration" types. Files can be decrypted and verified using the accompanying EncryptedCredentials.
  - **hash**: String (Required: True)
    - Base64-encoded element hash for using in PassportElementErrorUnspecified

💡 --- 💡

### 📦 EncryptedCredentials <a id='encryptedcredentials'></a>
- **URL**: [https://core.telegram.org/bots/api#encryptedcredentials](https://core.telegram.org/bots/api#encryptedcredentials)
- **Description**:
  - Describes data required for decrypting and authenticating EncryptedPassportElement. See the Telegram Passport Documentation for a complete description of the data decryption and authentication processes.
- **Fields**:
  - **data**: String (Required: True)
    - Base64-encoded encrypted JSON-serialized data with unique user's payload, data hashes and secrets required for EncryptedPassportElement decryption and authentication
  - **hash**: String (Required: True)
    - Base64-encoded data hash for data authentication
  - **secret**: String (Required: True)
    - Base64-encoded secret, encrypted with the bot's public RSA key, required for data decryption

💡 --- 💡

### 📦 PassportElementError <a id='passportelementerror'></a>
- **URL**: [https://core.telegram.org/bots/api#passportelementerror](https://core.telegram.org/bots/api#passportelementerror)
- **Description**:
  - This object represents an error in the Telegram Passport element which was submitted that should be resolved by the user. It should be one of:
  - - PassportElementErrorDataField
  - - PassportElementErrorFrontSide
  - - PassportElementErrorReverseSide
  - - PassportElementErrorSelfie
  - - PassportElementErrorFile
  - - PassportElementErrorFiles
  - - PassportElementErrorTranslationFile
  - - PassportElementErrorTranslationFiles
  - - PassportElementErrorUnspecified
- **Subtypes**:
  - PassportElementErrorDataField
  - PassportElementErrorFrontSide
  - PassportElementErrorReverseSide
  - PassportElementErrorSelfie
  - PassportElementErrorFile
  - PassportElementErrorFiles
  - PassportElementErrorTranslationFile
  - PassportElementErrorTranslationFiles
  - PassportElementErrorUnspecified

💡 --- 💡

### 📦 PassportElementErrorDataField <a id='passportelementerrordatafield'></a>
- **URL**: [https://core.telegram.org/bots/api#passportelementerrordatafield](https://core.telegram.org/bots/api#passportelementerrordatafield)
- **Description**:
  - Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes.
- **Fields**:
  - **source**: String (Required: True)
    - Error source, must be data
  - **type**: String (Required: True)
    - The section of the user's Telegram Passport which has the error, one of "personal_details", "passport", "driver_license", "identity_card", "internal_passport", "address"
  - **field_name**: String (Required: True)
    - Name of the data field which has the error
  - **data_hash**: String (Required: True)
    - Base64-encoded data hash
  - **message**: String (Required: True)
    - Error message

💡 --- 💡

### 📦 PassportElementErrorFrontSide <a id='passportelementerrorfrontside'></a>
- **URL**: [https://core.telegram.org/bots/api#passportelementerrorfrontside](https://core.telegram.org/bots/api#passportelementerrorfrontside)
- **Description**:
  - Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes.
- **Fields**:
  - **source**: String (Required: True)
    - Error source, must be front_side
  - **type**: String (Required: True)
    - The section of the user's Telegram Passport which has the issue, one of "passport", "driver_license", "identity_card", "internal_passport"
  - **file_hash**: String (Required: True)
    - Base64-encoded hash of the file with the front side of the document
  - **message**: String (Required: True)
    - Error message

💡 --- 💡

### 📦 PassportElementErrorReverseSide <a id='passportelementerrorreverseside'></a>
- **URL**: [https://core.telegram.org/bots/api#passportelementerrorreverseside](https://core.telegram.org/bots/api#passportelementerrorreverseside)
- **Description**:
  - Represents an issue with the reverse side of a document. The error is considered resolved when the file with reverse side of the document changes.
- **Fields**:
  - **source**: String (Required: True)
    - Error source, must be reverse_side
  - **type**: String (Required: True)
    - The section of the user's Telegram Passport which has the issue, one of "driver_license", "identity_card"
  - **file_hash**: String (Required: True)
    - Base64-encoded hash of the file with the reverse side of the document
  - **message**: String (Required: True)
    - Error message

💡 --- 💡

### 📦 PassportElementErrorSelfie <a id='passportelementerrorselfie'></a>
- **URL**: [https://core.telegram.org/bots/api#passportelementerrorselfie](https://core.telegram.org/bots/api#passportelementerrorselfie)
- **Description**:
  - Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes.
- **Fields**:
  - **source**: String (Required: True)
    - Error source, must be selfie
  - **type**: String (Required: True)
    - The section of the user's Telegram Passport which has the issue, one of "passport", "driver_license", "identity_card", "internal_passport"
  - **file_hash**: String (Required: True)
    - Base64-encoded hash of the file with the selfie
  - **message**: String (Required: True)
    - Error message

💡 --- 💡

### 📦 PassportElementErrorFile <a id='passportelementerrorfile'></a>
- **URL**: [https://core.telegram.org/bots/api#passportelementerrorfile](https://core.telegram.org/bots/api#passportelementerrorfile)
- **Description**:
  - Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes.
- **Fields**:
  - **source**: String (Required: True)
    - Error source, must be file
  - **type**: String (Required: True)
    - The section of the user's Telegram Passport which has the issue, one of "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration"
  - **file_hash**: String (Required: True)
    - Base64-encoded file hash
  - **message**: String (Required: True)
    - Error message

💡 --- 💡

### 📦 PassportElementErrorFiles <a id='passportelementerrorfiles'></a>
- **URL**: [https://core.telegram.org/bots/api#passportelementerrorfiles](https://core.telegram.org/bots/api#passportelementerrorfiles)
- **Description**:
  - Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.
- **Fields**:
  - **source**: String (Required: True)
    - Error source, must be files
  - **type**: String (Required: True)
    - The section of the user's Telegram Passport which has the issue, one of "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration"
  - **file_hashes**: Array of String (Required: True)
    - List of base64-encoded file hashes
  - **message**: String (Required: True)
    - Error message

💡 --- 💡

### 📦 PassportElementErrorTranslationFile <a id='passportelementerrortranslationfile'></a>
- **URL**: [https://core.telegram.org/bots/api#passportelementerrortranslationfile](https://core.telegram.org/bots/api#passportelementerrortranslationfile)
- **Description**:
  - Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes.
- **Fields**:
  - **source**: String (Required: True)
    - Error source, must be translation_file
  - **type**: String (Required: True)
    - Type of element of the user's Telegram Passport which has the issue, one of "passport", "driver_license", "identity_card", "internal_passport", "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration"
  - **file_hash**: String (Required: True)
    - Base64-encoded file hash
  - **message**: String (Required: True)
    - Error message

💡 --- 💡

### 📦 PassportElementErrorTranslationFiles <a id='passportelementerrortranslationfiles'></a>
- **URL**: [https://core.telegram.org/bots/api#passportelementerrortranslationfiles](https://core.telegram.org/bots/api#passportelementerrortranslationfiles)
- **Description**:
  - Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation change.
- **Fields**:
  - **source**: String (Required: True)
    - Error source, must be translation_files
  - **type**: String (Required: True)
    - Type of element of the user's Telegram Passport which has the issue, one of "passport", "driver_license", "identity_card", "internal_passport", "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration"
  - **file_hashes**: Array of String (Required: True)
    - List of base64-encoded file hashes
  - **message**: String (Required: True)
    - Error message

💡 --- 💡

### 📦 PassportElementErrorUnspecified <a id='passportelementerrorunspecified'></a>
- **URL**: [https://core.telegram.org/bots/api#passportelementerrorunspecified](https://core.telegram.org/bots/api#passportelementerrorunspecified)
- **Description**:
  - Represents an issue in an unspecified place. The error is considered resolved when new data is added.
- **Fields**:
  - **source**: String (Required: True)
    - Error source, must be unspecified
  - **type**: String (Required: True)
    - Type of element of the user's Telegram Passport which has the issue
  - **element_hash**: String (Required: True)
    - Base64-encoded element hash
  - **message**: String (Required: True)
    - Error message

💡 --- 💡

### 📦 Game <a id='game'></a>
- **URL**: [https://core.telegram.org/bots/api#game](https://core.telegram.org/bots/api#game)
- **Description**:
  - This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.
- **Fields**:
  - **title**: String (Required: True)
    - Title of the game
  - **description**: String (Required: True)
    - Description of the game
  - **photo**: Array of PhotoSize (Required: True)
    - Photo that will be displayed in the game message in chats.
  - **text**: String (Required: False)
    - Optional. Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls setGameScore, or manually edited using editMessageText. 0-4096 characters.
  - **text_entities**: Array of MessageEntity (Required: False)
    - Optional. Special entities that appear in text, such as usernames, URLs, bot commands, etc.
  - **animation**: Animation (Required: False)
    - Optional. Animation that will be displayed in the game message in chats. Upload via BotFather

💡 --- 💡

### 📦 CallbackGame <a id='callbackgame'></a>
- **URL**: [https://core.telegram.org/bots/api#callbackgame](https://core.telegram.org/bots/api#callbackgame)
- **Description**:
  - A placeholder, currently holds no information. Use BotFather to set up your game.

💡 --- 💡

### 📦 GameHighScore <a id='gamehighscore'></a>
- **URL**: [https://core.telegram.org/bots/api#gamehighscore](https://core.telegram.org/bots/api#gamehighscore)
- **Description**:
  - This object represents one row of the high scores table for a game.
- **Fields**:
  - **position**: Integer (Required: True)
    - Position in high score table for the game
  - **user**: User (Required: True)
    - User
  - **score**: Integer (Required: True)
    - Score

💡 --- 💡


---
📝 *Documentation auto-generated by Telegram Bot API Scraper*
