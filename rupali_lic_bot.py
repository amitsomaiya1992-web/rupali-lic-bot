from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    ContextTypes,
    filters
)

# ==================================
# BOT TOKEN
# ==================================

TOKEN = "8822019741:AAE_RJikhgZo9v61cWE9H3ZBI3QRgO2wVds"

# Tamaro Telegram Chat ID pachi mukishu
ADMIN_CHAT_ID = 631860445


# ==================================
# FORM QUESTION NUMBERS
# ==================================

(
    NAME,
    MOBILE,
    WHATSAPP,
    AGE,
    STATE,
    CITY,
    REQUIREMENT,
    BUDGET,
    MESSAGE
) = range(9)


# ==================================
# LANGUAGE BUTTONS
# ==================================

LANGUAGE_MENU = ReplyKeyboardMarkup(
    [
        ["ગુજરાતી", "हिंदी"],
        ["English"]
    ],
    resize_keyboard=True
)


# ==================================
# MAIN MENUS
# ==================================

GU_MENU = ReplyKeyboardMarkup(
    [
        ["📝 LIC જરૂરિયાત ફોર્મ"],
        ["📞 રૂપાલીનો સંપર્ક"],
        ["🧮 LIC પ્રીમિયમ કેલ્ક્યુલેટર"],
        ["🌐 ભાષા બદલો"]
    ],
    resize_keyboard=True
)


HI_MENU = ReplyKeyboardMarkup(
    [
        ["📝 LIC आवश्यकता फॉर्म"],
        ["📞 रूपाली से संपर्क"],
        ["🧮 LIC प्रीमियम कैलकुलेटर"],
        ["🌐 भाषा बदलें"]
    ],
    resize_keyboard=True
)


EN_MENU = ReplyKeyboardMarkup(
    [
        ["📝 LIC Requirement Form"],
        ["📞 Contact Rupali"],
        ["🧮 LIC Premium Calculator"],
        ["🌐 Change Language"]
    ],
    resize_keyboard=True
)


# ==================================
# LANGUAGE TEXT FUNCTION
# ==================================

def t(lang, gu, hi, en):

    if lang == "gu":
        return gu

    elif lang == "hi":
        return hi

    else:
        return en


def get_menu(lang):

    if lang == "gu":
        return GU_MENU

    elif lang == "hi":
        return HI_MENU

    else:
        return EN_MENU


# ==================================
# START
# ==================================

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "🙏 Rupali LIC Help માં આપનું સ્વાગત છે\n\n"
        "ભાષા પસંદ કરો\n"
        "भाषा चुनें\n"
        "Select your language",
        reply_markup=LANGUAGE_MENU
    )


# ==================================
# SELECT LANGUAGE
# ==================================

async def select_language(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    selected = update.message.text

    if selected == "ગુજરાતી":

        lang = "gu"

    elif selected == "हिंदी":

        lang = "hi"

    else:

        lang = "en"

    context.user_data["language"] = lang

    await update.message.reply_text(
        t(
            lang,

            "🙏 Rupali LIC Help માં આપનું સ્વાગત છે.\n\n"
            "કૃપા કરીને નીચેનો વિકલ્પ પસંદ કરો.",

            "🙏 Rupali LIC Help में आपका स्वागत है।\n\n"
            "कृपया नीचे दिया गया विकल्प चुनें।",

            "🙏 Welcome to Rupali LIC Help.\n\n"
            "Please select an option below."
        ),

        reply_markup=get_menu(lang)
    )


# ==================================
# START FORM
# ==================================

async def start_form(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    lang = context.user_data.get(
        "language",
        "en"
    )

    await update.message.reply_text(
        t(
            lang,

            "📝 LIC જરૂરિયાત ફોર્મ\n\n"
            "તમારી માહિતી Rupali LIC Advisor સાથે સંપર્ક માટે ઉપયોગમાં લેવાશે.\n\n"
            "પ્રશ્ન 1 / 9\n"
            "👤 તમારું પૂરું નામ લખો:",

            "📝 LIC आवश्यकता फॉर्म\n\n"
            "आपकी जानकारी Rupali LIC Advisor द्वारा संपर्क के लिए उपयोग की जाएगी।\n\n"
            "प्रश्न 1 / 9\n"
            "👤 अपना पूरा नाम लिखें:",

            "📝 LIC Requirement Form\n\n"
            "Your information will be used by Rupali LIC Advisor to contact you.\n\n"
            "Question 1 / 9\n"
            "👤 Enter your full name:"
        )
    )

    return NAME


# ==================================
# QUESTION 2
# ==================================

async def get_name(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    context.user_data["name"] = update.message.text

    lang = context.user_data.get(
        "language",
        "en"
    )

    await update.message.reply_text(
        t(
            lang,

            "પ્રશ્ન 2 / 9\n"
            "📱 તમારો Mobile Number લખો:",

            "प्रश्न 2 / 9\n"
            "📱 अपना Mobile Number लिखें:",

            "Question 2 / 9\n"
            "📱 Enter your mobile number:"
        )
    )

    return MOBILE


# ==================================
# QUESTION 3
# ==================================

async def get_mobile(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    context.user_data["mobile"] = update.message.text

    lang = context.user_data.get(
        "language",
        "en"
    )

    await update.message.reply_text(
        t(
            lang,

            "પ્રશ્ન 3 / 9\n"
            "💬 તમારો WhatsApp Number લખો.\n"
            "જો Mobile અને WhatsApp નંબર એક જ હોય તો એ જ નંબર લખો:",

            "प्रश्न 3 / 9\n"
            "💬 अपना WhatsApp Number लिखें।\n"
            "अगर Mobile और WhatsApp नंबर एक ही है तो वही नंबर लिखें:",

            "Question 3 / 9\n"
            "💬 Enter your WhatsApp number.\n"
            "If it is the same as your mobile number, enter the same number:"
        )
    )

    return WHATSAPP


# ==================================
# QUESTION 4
# ==================================

async def get_whatsapp(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    context.user_data["whatsapp"] = update.message.text

    lang = context.user_data.get(
        "language",
        "en"
    )

    await update.message.reply_text(
        t(
            lang,

            "પ્રશ્ન 4 / 9\n"
            "🎂 તમારી ઉંમર લખો:",

            "प्रश्न 4 / 9\n"
            "🎂 अपनी उम्र लिखें:",

            "Question 4 / 9\n"
            "🎂 Enter your age:"
        )
    )

    return AGE


# ==================================
# QUESTION 5
# ==================================

async def get_age(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    context.user_data["age"] = update.message.text

    lang = context.user_data.get(
        "language",
        "en"
    )

    await update.message.reply_text(
        t(
            lang,

            "પ્રશ્ન 5 / 9\n"
            "🗺️ તમારું State લખો:",

            "प्रश्न 5 / 9\n"
            "🗺️ अपना State लिखें:",

            "Question 5 / 9\n"
            "🗺️ Enter your state:"
        )
    )

    return STATE


# ==================================
# QUESTION 6
# ==================================

async def get_state(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    context.user_data["state"] = update.message.text

    lang = context.user_data.get(
        "language",
        "en"
    )

    await update.message.reply_text(
        t(
            lang,

            "પ્રશ્ન 6 / 9\n"
            "🏙️ તમારું City લખો:",

            "प्रश्न 6 / 9\n"
            "🏙️ अपना City लिखें:",

            "Question 6 / 9\n"
            "🏙️ Enter your city:"
        )
    )

    return CITY


# ==================================
# QUESTION 7 - REQUIREMENT
# ==================================

async def get_city(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    context.user_data["city"] = update.message.text

    lang = context.user_data.get(
        "language",
        "en"
    )

    if lang == "gu":

        keyboard = [
            ["💰 રોકાણ / બચત"],
            ["👶 બાળકનું ભવિષ્ય"],
            ["👴 નિવૃત્તિ / પેન્શન"],
            ["🛡️ પરિવાર સુરક્ષા / ઇન્શ્યોરન્સ"],
            ["📄 હાલની LIC પોલિસી મદદ"],
            ["❓ અન્ય જરૂરિયાત"]
        ]

        question = (
            "પ્રશ્ન 7 / 9\n"
            "🎯 તમને કઈ જરૂરિયાત વિશે માહિતી જોઈએ છે?"
        )

    elif lang == "hi":

        keyboard = [
            ["💰 निवेश / बचत"],
            ["👶 बच्चे का भविष्य"],
            ["👴 रिटायरमेंट / पेंशन"],
            ["🛡️ परिवार सुरक्षा / इंश्योरेंस"],
            ["📄 मौजूदा LIC पॉलिसी सहायता"],
            ["❓ अन्य आवश्यकता"]
        ]

        question = (
            "प्रश्न 7 / 9\n"
            "🎯 आपको किस आवश्यकता के बारे में जानकारी चाहिए?"
        )

    else:

        keyboard = [
            ["💰 Investment / Savings"],
            ["👶 Child Future Plan"],
            ["👴 Retirement / Pension"],
            ["🛡️ Family Protection / Insurance"],
            ["📄 Existing LIC Policy Help"],
            ["❓ Other Requirement"]
        ]

        question = (
            "Question 7 / 9\n"
            "🎯 What information do you need?"
        )

    await update.message.reply_text(
        question,

        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )
    )

    return REQUIREMENT


# ==================================
# QUESTION 8 - BUDGET
# ==================================

async def get_requirement(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    context.user_data["requirement"] = (
        update.message.text
    )

    lang = context.user_data.get(
        "language",
        "en"
    )

    if lang == "gu":

        keyboard = [
            ["₹1,000 થી ₹2,000 પ્રતિ મહિનો"],
            ["₹2,000 થી ₹5,000 પ્રતિ મહિનો"],
            ["₹5,000 થી ₹10,000 પ્રતિ મહિનો"],
            ["₹10,000+ પ્રતિ મહિનો"],
            ["🤔 હજુ નક્કી નથી"]
        ]

        question = (
            "પ્રશ્ન 8 / 9\n"
            "💰 તમારું અંદાજિત માસિક બજેટ પસંદ કરો:"
        )

    elif lang == "hi":

        keyboard = [
            ["₹1,000 से ₹2,000 प्रति माह"],
            ["₹2,000 से ₹5,000 प्रति माह"],
            ["₹5,000 से ₹10,000 प्रति माह"],
            ["₹10,000+ प्रति माह"],
            ["🤔 अभी तय नहीं है"]
        ]

        question = (
            "प्रश्न 8 / 9\n"
            "💰 अपना अनुमानित मासिक बजट चुनें:"
        )

    else:

        keyboard = [
            ["₹1,000 to ₹2,000 per month"],
            ["₹2,000 to ₹5,000 per month"],
            ["₹5,000 to ₹10,000 per month"],
            ["₹10,000+ per month"],
            ["🤔 Not decided yet"]
        ]

        question = (
            "Question 8 / 9\n"
            "💰 Select your estimated monthly budget:"
        )

    await update.message.reply_text(
        question,

        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )
    )

    return BUDGET


# ==================================
# QUESTION 9
# ==================================

async def get_budget(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    context.user_data["budget"] = (
        update.message.text
    )

    lang = context.user_data.get(
        "language",
        "en"
    )

    await update.message.reply_text(
        t(
            lang,

            "પ્રશ્ન 9 / 9\n"
            "📝 કોઈ વધારાનો પ્રશ્ન કે માહિતી હોય તો લખો.\n"
            "કંઈ ન હોય તો No લખો:",

            "प्रश्न 9 / 9\n"
            "📝 कोई अतिरिक्त प्रश्न या जानकारी हो तो लिखें।\n"
            "कुछ नहीं हो तो No लिखें:",

            "Question 9 / 9\n"
            "📝 Enter any additional question or information.\n"
            "If you have nothing to add, type No:"
        )
    )

    return MESSAGE


# ==================================
# SUBMIT FORM
# ==================================

async def submit_form(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    context.user_data["message"] = (
        update.message.text
    )

    data = context.user_data

    details = (
        "🔔 NEW LIC CUSTOMER ENQUIRY\n\n"

        f"👤 Name: {data.get('name')}\n"

        f"📱 Mobile: {data.get('mobile')}\n"

        f"💬 WhatsApp: {data.get('whatsapp')}\n"

        f"🎂 Age: {data.get('age')}\n"

        f"🗺️ State: {data.get('state')}\n"

        f"🏙️ City: {data.get('city')}\n\n"

        f"🎯 Requirement:\n"
        f"{data.get('requirement')}\n\n"

        f"💰 Budget:\n"
        f"{data.get('budget')}\n\n"

        f"📝 Additional Message:\n"
        f"{data.get('message')}"
    )


    # ADMIN CHAT ID pachi add karishu
    if ADMIN_CHAT_ID != 0:

        await context.bot.send_message(
            chat_id=ADMIN_CHAT_ID,
            text=details
        )


    lang = data.get(
        "language",
        "en"
    )

    await update.message.reply_text(
        t(
            lang,

            "✅ તમારી માહિતી સફળતાપૂર્વક મોકલવામાં આવી છે.\n\n"
            "👩‍💼 Rupali LIC Advisor ટૂંક સમયમાં તમારા WhatsApp પર સંપર્ક કરશે.",

            "✅ आपकी जानकारी सफलतापूर्वक भेज दी गई है।\n\n"
            "👩‍💼 Rupali LIC Advisor जल्द आपके WhatsApp पर संपर्क करेंगी।",

            "✅ Your information has been submitted successfully.\n\n"
            "👩‍💼 Rupali LIC Advisor will contact you on WhatsApp soon."
        ),

        reply_markup=get_menu(lang)
    )

    return ConversationHandler.END


# ==================================
# CONTACT RUPALI
# ==================================

async def contact(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    lang = context.user_data.get(
        "language",
        "en"
    )

    await update.message.reply_text(
        t(
            lang,

            "📞 Rupali Somaiya\n\n"
            "👩‍💼 LIC Advisor\n"
            "📱 Call / WhatsApp: 9998289297",

            "📞 Rupali Somaiya\n\n"
            "👩‍💼 LIC Advisor\n"
            "📱 Call / WhatsApp: 9998289297",

            "📞 Rupali Somaiya\n\n"
            "👩‍💼 LIC Advisor\n"
            "📱 Call / WhatsApp: 9998289297"
        )
    )


# ==================================
# CHANGE LANGUAGE
# ==================================

async def change_language(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "ભાષા પસંદ કરો\n"
        "भाषा चुनें\n"
        "Select your language",

        reply_markup=LANGUAGE_MENU
    )


# ==================================
# CANCEL
# ==================================

async def cancel(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    lang = context.user_data.get(
        "language",
        "en"
    )

    await update.message.reply_text(
        t(
            lang,
            "❌ ફોર્મ બંધ કરવામાં આવ્યું.",
            "❌ फॉर्म बंद कर दिया गया।",
            "❌ Form cancelled."
        ),

        reply_markup=get_menu(lang)
    )

    return ConversationHandler.END


# ==================================
# CREATE BOT
# ==================================

app = Application.builder().token(
    TOKEN
).build()


# ==================================
# FORM HANDLER
# ==================================

form_handler = ConversationHandler(

    entry_points=[

        MessageHandler(

            filters.Regex(
                r"^(📝 LIC જરૂરિયાત ફોર્મ|"
                r"📝 LIC आवश्यकता फॉर्म|"
                r"📝 LIC Requirement Form)$"
            ),

            start_form
        )
    ],

    states={

        NAME: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_name
            )
        ],

        MOBILE: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_mobile
            )
        ],

        WHATSAPP: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_whatsapp
            )
        ],

        AGE: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_age
            )
        ],

        STATE: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_state
            )
        ],

        CITY: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_city
            )
        ],

        REQUIREMENT: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_requirement
            )
        ],

        BUDGET: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_budget
            )
        ],

        MESSAGE: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                submit_form
            )
        ]
    },

    fallbacks=[

        CommandHandler(
            "cancel",
            cancel
        )
    ]
)


# ==================================
# ADD HANDLERS
# ==================================

app.add_handler(
    CommandHandler(
        "start",
        start
    )
)

app.add_handler(
    form_handler
)

app.add_handler(
    MessageHandler(
        filters.Regex(
            r"^(ગુજરાતી|हिंदी|English)$"
        ),
        select_language
    )
)

app.add_handler(
    MessageHandler(
        filters.Regex(
            r"^(📞 રૂપાલીનો સંપર્ક|"
            r"📞 रूपाली से संपर्क|"
            r"📞 Contact Rupali)$"
        ),
        contact
    )
)

app.add_handler(
    MessageHandler(
        filters.Regex(
            r"^(🌐 ભાષા બદલો|"
            r"🌐 भाषा बदलें|"
            r"🌐 Change Language)$"
        ),
        change_language
    )
)


# ==================================
# RUN BOT
# ==================================

print("Rupali LIC Form Bot is running...")

app.run_polling()
