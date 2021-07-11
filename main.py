from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler, ConversationHandler
from conf import TOKEN

from iymon import (
    DIN_VA_SHARIAT_NIMA,
    IYMON_NIMA,
    ALLOH_TAOLLOGA_IYMON,
    FARISHTALARGA_IYMON,
    ILOHIY_KITOBLARGA_IYMON,
    PAYGAMBARLARGA_IYMON,
    OXIRAT_KUNIGA_IYMON,
    QADARGA_IYMON,
    VAFOT_ETGANDAN_KEYIN_QAYATA_TIRILISHGA_IYMON,
    AQIDA,
    AHLI_SUNNA_VA_AHLI_JAMOA,
    HALOL_VA_HAROM
)

from haj import (
    HAJ_QANDAY_IBODAT,
    HAJNING_ODOBLARI,
    HAJNING_NOZIK_SIRLARI,
    HAJ_SAFARIGA_CHIQUVCHILARGA_TAVSIYALAR,
    HAJ_IBODATI_TURLARI,
    HAJ_IBODATI_TURLARI_2,
    HAJNING_FAPZ_VA_VOJIB_SUNNATLARI,
    EHROMGA_KIRISH,
    EHROMDAGI_AMALLAR_VA_UNING_KAFFORATLARI,
    EHROMDAGI_AMALLAR_VA_UNING_KAFFORATLARI_2,
    EHROMDAGI_AMALLAR_VA_UNING_KAFFORATLARI_3,
    TALBIYA_AYTISH,
    HARAMI_SHAROFGA_KIRISH,
    TAVOFNI_BOSHLASH,
    SAFO_VA_MARVA_QILISH_ORASIDA_SAY_QILISH,
    MINODA_TURISH,
    AROFATDA_TURISH,
    AROFATDA_TURISH_2,
    MUZDALIFADA_BOLISH,
    SHAYTONGA_TOSH_OTISH,
    SHAYTONGA_TOSH_OTISH_2,
    TAVOFNING_TURLARI,
    HAJNING_BESH_KUNI,
    HAJNING_BESH_KUNI_2,
    BADAL_HAJI,
)

from namoz import (
    FIYL_SURASI,
    NAMOZGA_POKLANISH,
    GUSUL,
    GUSUL_QANDAY_QILINADI,
    GUSUL_QILISH_FARZ_BULGAN_HALATLAR,
    GUSUL_QILISH_SUNNAT_BULGAN_HALATLAR,
    GUSUL_QILISH_MUSTAHAB_BULGAN_HALATLAR,
    GUSULNING_FARZLARI_VA_SUNNATLARI,
    GUSUL_HAQIDA,
    TAHORAT,
    TAHORATNING_SHARTLARI,
    SHARIAT_ISTILOHIDA_TAHORAT_IKKI_QISIMGA_BULINADI,
    TAHORATNING_FARZLARI,
    TAHORATNING_SUNNATLARI,
    TAHORATNING_ODOBLARI,
    TAHORATNING_MAKRUHLARI,
    TAHORATNI_SINDIRUVCHI_NARSALAR,
    TAYAMMUM,
    TAYAMMUMNING_SHARTLARI,
    TAYAMMUMNING_RUKNLARI,
    TAYAMMUM_QILISH_TARTIBI,
    TAYAMMUMNING_FARZLARI,
    TAYAMMUMNING_SUNNATLARI,
    TAYAMMUMNI_BUZUVCHI_NARSALAR,
    NAMOZ,
    NAMOZ_2,
    NAMOZNING_BOSHQA_FOYDALARI,
    NAMOZNING_BOSHQA_FOYDALARI_2,
    AMALLARINING_HUKUMLARI,
    NAMOZADAGI_HOLATLAR,
    NAMOZADAGI_HOLATLAR_2,
    NAMOZNING_TURLARI,
    NAMOZNING_VAQTLARI,
    NAMOZ_RAKATLARI,
    AZON_VA_IQOMAT,
    IKKI_RAKAT_FARZ_NAMOZINI_OQISH,
    TORT_RAKATLI_FARZ_NAMOZINI_OQISH_TARTIBI,
    UCH_RAKATLI_FARZ_NAMOZINI_OQISH_TARTIBI,
    TORT_RAKATLI_SUNNAT_NAMOZINI_OQISH_TARTIBI,
    NAMOZDAGI_FARZ_AMALLARI,
    NAMOZNING_VOJIBLARI,
    NAMOZNING_SUNNATLARI,
    NAMOZNING_MUSTAHABLARI,
    NAMOZDAGI_HAROM_AMAALLAR,
    NAMOZNING_MUBOHLARI,
    NAMOZNI_BUZUVCHI_AMALLAR,
    NAMOZDAGI_MAKRUH_AMALLAR,
    MAKRUH_BOLMAGAN_AMALLAR,
    NAMOZNING_ODOBLARI,
    QIBLA,
    SAJDAI_SAHV,
    SAJDAI_SAHV_2,
    SAJDAI_SAHV_3,
    SAJDAI_SAHV_4,
    SUTRA,
    NAMOZDAGI_OQILADIGAN_KICHIK_SURALAR,
    FOTIHA_SURASI,
    QURAYSH_SURASI,
    MAUN_SURASI,
    KAVSAR_SURASI,
    KAFIRUN_SURASI,
    NASR_SURASI,
    MASAD_SURASI,
    IXLOS_SURASI,
    FALAQA_SURASI,
    ANNAS_SURASI,
    KURSIY_OYATI,
    SANO,
    TASHAHHUD,
    SALOVATLAR,
    QUNUT_DUOSI,
    NAMOZDAN_SUNG_OQILADIGAN_DUOLAR,
    JAMOAT_NAMOZI,
    JAMOAT_NAMOZI_2,
    JAMOAT_NAMOZI_3,
    NAMOZDAGI_SAFLAR_TARTIBI,
    IMOMLIKKA_KILAR_LAYOQATLI,
    MASJID_ODOBLARI,
    MASJID_ODOBLARI_2,
    MASJID_ODOBLARI_3,
    MASJID_ODOBLARI_4,
    MASJID_ODOBLARI_5,
    QAZO_NAMOZLARINI_ADO_ETISH,
    QAZO_NAMOZLARINI_ADO_ETISH_2,
    TURLI_NAMOZLAR,
    VITIR_NAMOZI,
    TAROVEH_NAMOZI,
    TAROVEH_NAMOZI_2,
    MUSOFIRNING_NAMOZI,
    MUSOFIRNING_NAMOZI_2,
    JUMA_NAMOZI,
    JUMA_NAMOZI_2,
    JUMA_NAMOZI_3,
    JANOZA_NAMOZI,
    JANOZA_NAMOZI_2,
    JANOZA_NAMOZI_3,
    JANOZA_NAMOZI_4,
    JANOZA_NAMOZI_5,
    IKKI_IYD_NAMOZI,
    IKKI_IYD_NAMOZI_2,
    IKKI_IYD_NAMOZI_3,
    BEMOR_KISHINING_NAMOZI,
    XAVF_NAMOZI,
    QUYOSH_VA_OY_TUTILGANDAGI_NAMOZLAR,
    ISTIQO_NAMOZI,
    NAFL_NAMOZLAR,
    TAHIYYATUL_MASJID_NAMOZI,
    SHURUQ_NAMOZI,
    ZUHO_NAMOZI,
    SHUKRI_VUZU_NAMOZI,
    ISTIHORA_NAMOZI,
    HAJOAT_NAMOZI,
    TAVBA_NAMOZI,
    AVOBBIYN_NAMOZI,
    TAHAJJUD_NAMOZI,
    TASBEH_NAMOZI,
    NAFL_NAMOZLARINI_OQISH_TARTIBIB,
    NAFL_NAMOZLARINI_OQISH_TARTIBIB_2,
    MARKABDA_NAMOZ_OQISH,
    ETIKOF_OTIRISH,
    TILOVAT_SAJDASI,
    TILOVAT_SAJDASI_2,
    TILOVAT_SAJDASI_3,
    IBRATLI_NAMOZLAR,
    IBRATLI_NAMOZLAR_2,
    ROSHID_XALIFALARNING_NAMOZLARI,
    SAHOBA_VA_TOBEINLARNING_NAMOZLARI,
    SAHOBA_VA_TOBEINLARNING_NAMOZLARI_2,
    AVLIYOLAR_VA_ALLOMALRNING_NAMOZLARI,
)
from roza import (
    ROZA_QANDAY_IBODAT,
    ROZANING_DARAJALARI,
    ROZANING_SHARTLARI,
    ROZANING_TURLARI,
    ROZANI_TUTISH_HAROM_BOLGAN_KUNLAR,
    ROZANI_TUTISH_MAKRUH_BOLGAN_KUNLAR,
    ROZANING_NIYATLARI,
    SAHARLIK_VA_IFTORLIK,
    ROZANING_MUSTAHABLARI,
    ROZANI_BUZADIGAN_NARSALAR,
    ROZANI_BUZADIGAN_NARSALAR_2,
)

from zakot import (
    ZAKOT_NIMA,
    ZAKOTNING_FIQHIY_HUKUMLARI,
    CHORVA_HAYVONLARNING_HUKUMLARI,
    TILLA_VAKUMUSHNING_ZAKOTI,
    NAQT_PULDAN_OLINADIGAN_ZAKOT,
    TIJORAT_MOLIDAN_OLNADIGAN_ZAKOT,
    BUYUMLARDAN_OLNADIGAN_ZAKOT,
    QIMMATBAHO_TOSHLARNING_ZAKOTI,
    ZAKOT_OLISHI_MUMKIN_BOLMAGANLAR,
    ZAKOT_BERUVCHILARNING_VAZIFALARI,
)

ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, ELEVEN, TWELVE, THIRTEEN, FOURTEEN, FIFTEEN, SIXTEEN, SEVENTEEN, EIGHTEEN, NINETEEN = range(
    19)
FIRST, SECOND, THIRD = range(3)


def hello(update: Update, context: CallbackContext):
    buttons = [
        [
            InlineKeyboardButton('☪️ Iymon', callback_data='Iymon'),
            InlineKeyboardButton('🕌 Namoz', callback_data='Namoz'),
        ],
        [
            InlineKeyboardButton('💰 Zakot', callback_data='Zakot'),
            InlineKeyboardButton('🤲🏻 Ro\'za', callback_data='Ro\'za'),
        ],
        [
            InlineKeyboardButton('🕋 Haj', callback_data='Haj'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    update.message.reply_html(
        f'Assalomu alaykum va rohmatullohi va barokatuh \n🔰 Hurmatli aziz foydalanuvchimiz {update.effective_user.first_name}\n\nSiz ilk tashrif buyurgan telegram bot ISLOM dinining besh asosiy ustuni \n☪️ Iymon\n🕌 Namoz\n💰 Zakot\n🤲🏻 Ro\'za\n🕋 Haj\nshular haqida bilimlarni yanada boyitish va yanada ma\'naviy ozuqa olish maqsadida tayyorlandi.Ma\'lumotlar \"islom.uz\"🇺🇿  sayti orqali olindi.',
        reply_markup=reply_markup)
    return FIRST


def hello_over(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('☪️ Iymon', callback_data='Iymon'),
            InlineKeyboardButton('🕌 Namoz', callback_data='Namoz'),
        ],
        [
            InlineKeyboardButton('💰 Zakot', callback_data='Zakot'),
            InlineKeyboardButton('🤲🏻 Ro\'za', callback_data='Ro\'za'),
        ],
        [
            InlineKeyboardButton('🕋 Haj', callback_data='Haj'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(
        f'Assalomu alaykum va rohmatullohi va barokatuh \n🔰 Hurmatli aziz foydalanuvchimiz {update.effective_user.first_name}\n\nSiz ilk tashrif buyurgan telegram bot ISLOM dinining besh asosiy ustuni \n☪️ Iymon\n🕌 Namoz\n💰 Zakot\n🤲🏻 Ro\'za\n🕋 Haj\nshular haqida bilimlarni yanada boyitish va yanada ma\'naviy ozuqa olish maqsadida tayyorlandi.Ma\'lumotlar \"islom.uz\"🇺🇿  sayti orqali olindi.',
        reply_markup=reply_markup)
    return FIRST


# ******************************************* iymon_boshlanishi *******************************************
def dvsh(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(DIN_VA_SHARIAT_NIMA, reply_markup=reply_markup)
    return FIRST


def iyn(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(IYMON_NIMA, reply_markup=reply_markup)
    return FIRST


def ati(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(ALLOH_TAOLLOGA_IYMON, reply_markup=reply_markup)
    return FIRST


def fi(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(FARISHTALARGA_IYMON, reply_markup=reply_markup)
    return FIRST


def iki(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(ILOHIY_KITOBLARGA_IYMON, reply_markup=reply_markup)
    return FIRST


def pi(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(PAYGAMBARLARGA_IYMON, reply_markup=reply_markup)
    return FIRST


def oki(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(OXIRAT_KUNIGA_IYMON, reply_markup=reply_markup)
    return FIRST


def qi(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(QADARGA_IYMON, reply_markup=reply_markup)
    return FIRST


def osi(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(VAFOT_ETGANDAN_KEYIN_QAYATA_TIRILISHGA_IYMON, reply_markup=reply_markup)
    return FIRST


def aqida(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(AQIDA, reply_markup=reply_markup)
    return FIRST


def asvj(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(AHLI_SUNNA_VA_AHLI_JAMOA, reply_markup=reply_markup)
    return FIRST


def hah(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(HALOL_VA_HAROM, reply_markup=reply_markup)
    return FIRST


def one(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('☪️ Din va Shariat nima?', callback_data='dvsh'),
            InlineKeyboardButton('☪️ Iymon nima?', callback_data='iyn'),
        ],
        [
            InlineKeyboardButton('☪️ Alloh taologa iymon', callback_data='ati'),
            InlineKeyboardButton('☪️ Farishtalarga iymon', callback_data='fi'),
        ],
        [
            InlineKeyboardButton('☪️ Ilohiy kitoblarga iymon', callback_data='iki'),
            InlineKeyboardButton('☪️ Payg\'ambarlarga iymon', callback_data='pi'),
        ],
        [
            InlineKeyboardButton('☪️ Oxirat kuniga iymon', callback_data='oki'),
            InlineKeyboardButton('☪️ Qadarga iymon', callback_data='qi'),
        ],
        [
            InlineKeyboardButton('☪️ O\'lgandan so\'ng iymon', callback_data='osi'),
            InlineKeyboardButton('☪️ Aqida', callback_data='aqida'),
        ],
        [
            InlineKeyboardButton('☪️ Ahli sunna val jamoa', callback_data='asvj'),
            InlineKeyboardButton('☪️ Halol va Harom', callback_data='hah')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(
        '☪️ IYMON DARSLARI\n\n📖 Shayx Muhammad Sodiq Muhammad Yusuf xazratlarining \"Mo\'mining me\'roji\" nomli kitobi asosida tayyorlandi.',
        reply_markup=reply_markup)
    return FIRST


# *********************************************** iymon_oxirgi_qisim ***********************************************************


# ************************************************ namoz_boshlanishi ***********************************************************

def np_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_n')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NAMOZGA_POKLANISH, reply_markup=reply_markup)
    return FIRST


# ********************************** gusulni ichi *******************************************

def qhgq_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [

        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_m')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(GUSUL_QANDAY_QILINADI, reply_markup=reply_markup)
    return FIRST


def gqfbh_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [

        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_m')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(GUSUL_QILISH_FARZ_BULGAN_HALATLAR, reply_markup=reply_markup)
    return FIRST


def gqsbh_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [

        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_m')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(GUSUL_QILISH_SUNNAT_BULGAN_HALATLAR, reply_markup=reply_markup)
    return FIRST


def gqmbh_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [

        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_m')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(GUSUL_QILISH_MUSTAHAB_BULGAN_HALATLAR, reply_markup=reply_markup)
    return FIRST


def gfvs_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [

        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_m')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(GUSULNING_FARZLARI_VA_SUNNATLARI, reply_markup=reply_markup)
    return FIRST


def gh_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [

        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_m')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(GUSUL_HAQIDA, reply_markup=reply_markup)
    return FIRST


def gusul_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('🕌 Qanday hollarda g\'usil qilinadi', callback_data='qhgq'),
            InlineKeyboardButton('🕌 G\'usil qilish farz bo\'lgan holatlar', callback_data='gqfbh'),
        ],
        [
            InlineKeyboardButton('🕌 G\'usil qilish sunnat bo\'lgan hollar', callback_data='gqsbh'),
            InlineKeyboardButton('🕌 G\'usil qilish mustahab bo\'lgan holatlar', callback_data='gqmbh'),
        ],
        [
            InlineKeyboardButton('🕌 G\'usulning farzlari va sunnatlari', callback_data='gfvs'),
            InlineKeyboardButton('🕌 G\'usil haqida', callback_data='gh'),
        ],
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_n')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(GUSUL, reply_markup=reply_markup)
    return FIRST


# ****************************************** gusulni tugashi **************************************************
def taxsh_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [

        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_t')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TAHORATNING_SHARTLARI, reply_markup=reply_markup)
    return FIRST


def shitiqb_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [

        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_t')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(SHARIAT_ISTILOHIDA_TAHORAT_IKKI_QISIMGA_BULINADI, reply_markup=reply_markup)
    return FIRST


def taxf_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [

        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_t')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TAHORATNING_FARZLARI, reply_markup=reply_markup)
    return FIRST


def taxs_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [

        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_t')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TAHORATNING_SUNNATLARI, reply_markup=reply_markup)
    return FIRST


def taxo_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [

        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_t')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TAHORATNING_ODOBLARI, reply_markup=reply_markup)
    return FIRST


def taxm_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [

        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_t')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TAHORATNING_MAKRUHLARI, reply_markup=reply_markup)
    return FIRST


def taxsn_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [

        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_t')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TAHORATNI_SINDIRUVCHI_NARSALAR, reply_markup=reply_markup)
    return FIRST


def tahorat_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('🕌 Tahoratning shartlari', callback_data='taxsh'),
            InlineKeyboardButton('🕌 Shariat islohida tahorat ikki qismga bo\'linadi', callback_data='shitiqb')
        ],
        [
            InlineKeyboardButton('🕌 Tahoratning farzlari', callback_data='taxf'),
            InlineKeyboardButton('🕌 Tahoratning sunnatlari', callback_data='taxs')
        ],
        [
            InlineKeyboardButton('🕌 Tahoratning odoblari', callback_data='taxo'),
            InlineKeyboardButton('🕌 Tahoratning makruhlari', callback_data='taxm')
        ],
        [
            InlineKeyboardButton('🕌 Tahoratni sindiruvchi narsalar', callback_data='taxsn'),
        ],
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_n')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TAHORAT, reply_markup=reply_markup)
    return FIRST


# ************************************************ tahorat tugashi ********************************************

# ************************************************ tayammum **************************************************
def tsh_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tay')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TAYAMMUMNING_SHARTLARI, reply_markup=reply_markup)
    return FIRST


def tr_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tay')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TAYAMMUMNING_RUKNLARI, reply_markup=reply_markup)
    return FIRST


def tqt_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tay')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TAYAMMUM_QILISH_TARTIBI, reply_markup=reply_markup)
    return FIRST


def tf_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tay')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TAYAMMUMNING_FARZLARI, reply_markup=reply_markup)
    return FIRST


def ts_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tay')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TAYAMMUMNING_SUNNATLARI, reply_markup=reply_markup)
    return FIRST


def tbn_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tay')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TAYAMMUMNI_BUZUVCHI_NARSALAR, reply_markup=reply_markup)
    return FIRST


def tayammum_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('🕌 Tayammumning shartlari', callback_data='tsh'),
            InlineKeyboardButton('🕌 Tayammumning ruknlari', callback_data='tr'),
        ],
        [
            InlineKeyboardButton('🕌 Tayammum qilish tartibi', callback_data='tqt'),
            InlineKeyboardButton('🕌 Tayammumning farzlari', callback_data='tf'),
        ],
        [
            InlineKeyboardButton('🕌 Tayammumning sunnatlari', callback_data='ts'),
            InlineKeyboardButton('🕌 Tayammumni buzuvchi narsalar', callback_data='tbn'),
        ],
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_n')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TAYAMMUM, reply_markup=reply_markup)
    return FIRST


# ******************************************** tayammum tugashi *********************************************

# ******************************************** namoz qismi **************************************************
def nbf_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NAMOZNING_BOSHQA_FOYDALARI, reply_markup=reply_markup)
    return FIRST


def nbf_2_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NAMOZNING_BOSHQA_FOYDALARI_2, reply_markup=reply_markup)
    return FIRST


def ah_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(AMALLARINING_HUKUMLARI, reply_markup=reply_markup)
    return FIRST


def nh_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NAMOZADAGI_HOLATLAR, reply_markup=reply_markup)
    return FIRST


def nh_2_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NAMOZADAGI_HOLATLAR_2, reply_markup=reply_markup)
    return FIRST


def nt_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NAMOZNING_TURLARI, reply_markup=reply_markup)
    return FIRST


def nv_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NAMOZNING_VAQTLARI, reply_markup=reply_markup)
    return FIRST


def nr_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NAMOZ_RAKATLARI, reply_markup=reply_markup)
    return FIRST


def avi_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(AZON_VA_IQOMAT, reply_markup=reply_markup)
    return FIRST


def irfnot_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(IKKI_RAKAT_FARZ_NAMOZINI_OQISH, reply_markup=reply_markup)
    return FIRST


def trfnot_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TORT_RAKATLI_FARZ_NAMOZINI_OQISH_TARTIBI, reply_markup=reply_markup)
    return FIRST


def urfnot_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(UCH_RAKATLI_FARZ_NAMOZINI_OQISH_TARTIBI, reply_markup=reply_markup)
    return FIRST


def ss_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(SAJDAI_SAHV, reply_markup=reply_markup)
    return FIRST


def ss_2_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(SAJDAI_SAHV_2, reply_markup=reply_markup)
    return FIRST


def ss_3_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(SAJDAI_SAHV_3, reply_markup=reply_markup)
    return FIRST


def ss_4_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(SAJDAI_SAHV_4, reply_markup=reply_markup)
    return FIRST


def sutra_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(SUTRA, reply_markup=reply_markup)
    return FIRST


def nvojib_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NAMOZNING_VOJIBLARI, reply_markup=reply_markup)
    return FIRST


def ns_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NAMOZNING_SUNNATLARI, reply_markup=reply_markup)
    return FIRST


def nm_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NAMOZNING_MUSTAHABLARI, reply_markup=reply_markup)
    return FIRST


def nha_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NAMOZDAGI_HAROM_AMAALLAR, reply_markup=reply_markup)
    return FIRST


def nmrea_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NAMOZNING_MUBOHLARI, reply_markup=reply_markup)
    return FIRST


def nbamallar_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NAMOZNI_BUZUVCHI_AMALLAR, reply_markup=reply_markup)
    return FIRST


def nma_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NAMOZDAGI_MAKRUH_AMALLAR, reply_markup=reply_markup)
    return FIRST


def mba_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(MAKRUH_BOLMAGAN_AMALLAR, reply_markup=reply_markup)
    return FIRST


def no_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NAMOZNING_ODOBLARI, reply_markup=reply_markup)
    return FIRST


def qibla_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(QIBLA, reply_markup=reply_markup)
    return FIRST


def nfa_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NAMOZDAGI_FARZ_AMALLARI, reply_markup=reply_markup)
    return FIRST


def trsnot_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TORT_RAKATLI_SUNNAT_NAMOZINI_OQISH_TARTIBI, reply_markup=reply_markup)
    return FIRST


def namoz_2_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_namoz'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh'),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NAMOZ_2, reply_markup=reply_markup)
    return FIRST


def namoz_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('🕌 Namoz 2-qism', callback_data='namoz_2'),
        ],
        [
            InlineKeyboardButton('🕌 Namozning boshqa foydalari', callback_data='nbf'),
            InlineKeyboardButton('🕌 Namozning boshqa foydalari 2-qism', callback_data='nbf_2'),
        ],
        [
            InlineKeyboardButton('🕌 Namozdagi holatlar', callback_data='nh'),
            InlineKeyboardButton('🕌 Namozdagi holatlar 2-qism', callback_data='nh_2'),
        ],
        [
            InlineKeyboardButton('🕌 Namoz vaqtlari', callback_data='nv'),
            InlineKeyboardButton('🕌 Namoz rakatlari', callback_data='nr'),
        ],
        [
            InlineKeyboardButton('🕌 Azon va iqomat', callback_data='avi'),
            InlineKeyboardButton('🕌 Ikki rakatli farz namozini o\'qish tartibi', callback_data='irfnot'),
        ],
        [
            InlineKeyboardButton('🕌 To\'rt rakatli farz namozini o\'qish tartibi', callback_data='trfnot'),
            InlineKeyboardButton('🕌 Uch rakatli farz nomozni o\'qish tartibi', callback_data='urfnot'),
        ],
        [
            InlineKeyboardButton('🕌 Sajdai sahv', callback_data='ss'),
            InlineKeyboardButton('🕌 Sajdai sahv 2-qism', callback_data='ss_2'),
        ],
        [
            InlineKeyboardButton('🕌 Sajdai sahv 3-qism', callback_data='ss_3'),
            InlineKeyboardButton('🕌 Sajdai sahv 4-qism', callback_data='ss_4'),
        ],
        [
            InlineKeyboardButton('🕌 Namozning vojiblari', callback_data='nvojib'),
            InlineKeyboardButton('🕌 Namozning sunnatlari', callback_data='ns'),
        ],
        [
            InlineKeyboardButton('🕌 Namozning mustahablari', callback_data='nm'),
            InlineKeyboardButton('🕌 Namozdagi haram amallar', callback_data='nha'),
        ],
        [
            InlineKeyboardButton('🕌 Namozning mubahlari(ruxsat etilmagan ammallar)', callback_data='nmrea'),
            InlineKeyboardButton('🕌 Namozni buzuvchi amallar', callback_data='nbamallar'),
        ],
        [
            InlineKeyboardButton('🕌 Namozning makruh amallari', callback_data='nma'),
            InlineKeyboardButton('🕌 Makruh bo\'lmagan amallar', callback_data='mba'),
        ],
        [
            InlineKeyboardButton('🕌 Namozning odoblari', callback_data='no'),
            InlineKeyboardButton('🕌 Qibla', callback_data='qibla'),
        ],
        [
            InlineKeyboardButton('🕌 To\'rt rakatli sunnat namozini o\'qish tartibi', callback_data='trsnot'),
            InlineKeyboardButton('🕌 Namozdagi farz amallar', callback_data='nfa'),
        ],
        [
            InlineKeyboardButton('🕌 Namozning turlari', callback_data='nt'),
            InlineKeyboardButton('🕌 Amallarning hukumlari', callback_data='ah'),
        ],
        [
            InlineKeyboardButton('🕌 Sutra', callback_data='sutra'),
        ],
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_n')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],

    ]

    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NAMOZ, reply_markup=reply_markup)
    return FIRST


# ********************************************** namozni tugatish qismi  **********************************************

# ********************************************** Suralar boshi ********************************************************
def fos_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_noksvd')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(FOTIHA_SURASI, reply_markup=reply_markup)
    return FIRST


def fis_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_noksvd')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(FIYL_SURASI, reply_markup=reply_markup)
    return FIRST


def qus_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_noksvd')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(QURAYSH_SURASI, reply_markup=reply_markup)
    return FIRST


def mas_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_noksvd')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(MAUN_SURASI, reply_markup=reply_markup)
    return FIRST


def kas_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_noksvd')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(KAVSAR_SURASI, reply_markup=reply_markup)
    return FIRST


def kafs_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_noksvd')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(KAFIRUN_SURASI, reply_markup=reply_markup)
    return FIRST


def nas_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_noksvd')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NASR_SURASI, reply_markup=reply_markup)
    return FIRST


def maqs_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_noksvd')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(MASAD_SURASI, reply_markup=reply_markup)
    return FIRST


def fals_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_noksvd')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(FALAQA_SURASI, reply_markup=reply_markup)
    return FIRST


def ans_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_noksvd')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(ANNAS_SURASI, reply_markup=reply_markup)
    return FIRST


def ixs_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_noksvd')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(IXLOS_SURASI, reply_markup=reply_markup)
    return FIRST


def sano_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_noksvd')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(SANO, reply_markup=reply_markup)
    return FIRST


def tashahhud_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_noksvd')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TASHAHHUD, reply_markup=reply_markup)
    return FIRST


def salovat_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_noksvd')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(SALOVATLAR, reply_markup=reply_markup)
    return FIRST


def qud_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_noksvd')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(QUNUT_DUOSI, reply_markup=reply_markup)
    return FIRST


def kook_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_noksvd')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(KURSIY_OYATI, reply_markup=reply_markup)
    return FIRST


def noksvd_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    buttons = [
        [
            InlineKeyboardButton('📜 Fotiha surasi', callback_data='fos'),
            InlineKeyboardButton('📜Fiyl surasi', callback_data='fis'),
        ],
        [
            InlineKeyboardButton('📜 Quraysh surasi', callback_data='qus'),
            InlineKeyboardButton('📜 Ma\'un surasi', callback_data='mas'),
        ],
        [
            InlineKeyboardButton('📜 Kavsar surasi', callback_data='kas'),
            InlineKeyboardButton('📜 Kafirun surasi', callback_data='kafs'),
        ],
        [
            InlineKeyboardButton('📜 Nasr surasi', callback_data='nas'),
            InlineKeyboardButton('📜 Maqsad surasi', callback_data='maqs'),
        ],
        [
            InlineKeyboardButton('📜 Falaq surasi', callback_data='fals'),
            InlineKeyboardButton('📜 An-nas surasi', callback_data='ans'),
        ],
        [
            InlineKeyboardButton('📜 Ixlos surasi', callback_data='ixs'),
            InlineKeyboardButton('📜 Sano', callback_data='sano'),
        ],
        [
            InlineKeyboardButton('📜 Tashahhud (at-tahiyat)', callback_data='tashahhud'),
            InlineKeyboardButton('📜 Salovatlar', callback_data='salovat'),
        ],
        [
            InlineKeyboardButton('📜 Qunut duosi', callback_data='qud'),
            InlineKeyboardButton('📜 Kursiy oyati(oyatul-kursiy)', callback_data='kook'),
        ],
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_n')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NAMOZDAGI_OQILADIGAN_KICHIK_SURALAR, reply_markup=reply_markup)
    return FIRST


# ******************************************* Suralar tugashi ***********************************************

# ********************************** Namozdan song oqiladigan duo *******************************************
def nsod_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_n')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NAMOZDAN_SUNG_OQILADIGAN_DUOLAR, reply_markup=reply_markup)
    return FIRST


# ********************************** Namozdan song oqiladigan duo tugashi ***********************************


# ********************************** Janoza Namozi ***********************************
def nst_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_jn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NAMOZDAGI_SAFLAR_TARTIBI, reply_markup=reply_markup)
    return FIRST


def imkl_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_jn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(IMOMLIKKA_KILAR_LAYOQATLI, reply_markup=reply_markup)
    return FIRST


def masodob_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_jn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(MASJID_ODOBLARI, reply_markup=reply_markup)
    return FIRST


def masodob_2_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_jn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(MASJID_ODOBLARI_2, reply_markup=reply_markup)
    return FIRST


def masodob_3_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_jn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(MASJID_ODOBLARI_3, reply_markup=reply_markup)
    return FIRST


def masodob_4_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_jn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(MASJID_ODOBLARI_4, reply_markup=reply_markup)
    return FIRST


def masodob_5_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_jn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(MASJID_ODOBLARI_5, reply_markup=reply_markup)
    return FIRST


def jn_2_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_jn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(JAMOAT_NAMOZI_2, reply_markup=reply_markup)
    return FIRST


def jn_3_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_jn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(JAMOAT_NAMOZI_3, reply_markup=reply_markup)
    return FIRST


def jn_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('🕌 Jamoat namozi 2-qism', callback_data='jn_2'),
            InlineKeyboardButton('🕌 Jamoat namozi 3-qism', callback_data='jn_3'),
        ],
        [
            InlineKeyboardButton('🕌 Namozdagi saflar tartibi', callback_data='nst'),
            InlineKeyboardButton('🕌 Imomlikka kimlar layoqatli?', callback_data='imkl'),
        ],
        [
            InlineKeyboardButton('🕌 Masjid odoblari_1', callback_data='masodob'),
            InlineKeyboardButton('🕌 Masjid odoblari_2', callback_data='masodob_2'),
        ],
        [
            InlineKeyboardButton('🕌 Masjid odoblari_3', callback_data='masodob_3'),
            InlineKeyboardButton('🕌 Masjid odoblari_4', callback_data='masodob_4'),
        ],
        [
            InlineKeyboardButton('🕌 Masjid odoblari_5', callback_data='masodob_5'),
        ],
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_n')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(JAMOAT_NAMOZI, reply_markup=reply_markup)
    return FIRST


# ********************************** Janoza Namozi tugashi ***********************************

# ***********************************Ibratli namozlar boshlanishi ****************************************
def rxn_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_in')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(ROSHID_XALIFALARNING_NAMOZLARI, reply_markup=reply_markup)
    return FIRST


def svtn_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_in')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(SAHOBA_VA_TOBEINLARNING_NAMOZLARI, reply_markup=reply_markup)
    return FIRST


def svtn_2_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_in')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(SAHOBA_VA_TOBEINLARNING_NAMOZLARI_2, reply_markup=reply_markup)
    return FIRST


def avan_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_in')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(AVLIYOLAR_VA_ALLOMALRNING_NAMOZLARI, reply_markup=reply_markup)
    return FIRST


def in_2_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_in')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(IBRATLI_NAMOZLAR_2, reply_markup=reply_markup)
    return FIRST


def in_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('🕌 Ibratli namozlar 2-qism', callback_data='in_2'),
            InlineKeyboardButton('🕌 Roshid xalifalarning namozi', callback_data='rxn'),
        ],
        [
            InlineKeyboardButton('🕌 Sahoba va tobe\'inlarning namozi', callback_data='svtn'),
            InlineKeyboardButton('🕌 Sahoba va tobe\'inlarning namozi 2-qism', callback_data='svtn_2'),
        ],
        [
            InlineKeyboardButton('🕌 Avliyolar va allomalarning namozi', callback_data='avan'),
        ],
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_n')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(IBRATLI_NAMOZLAR, reply_markup=reply_markup)
    return FIRST


# ***********************************Ibratli namozlar tugashi ********************************************


# *********************************** qazo namozini ado etish boshlanishi ********************************************
def qnae_2_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_qnae')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(QAZO_NAMOZLARINI_ADO_ETISH_2, reply_markup=reply_markup)
    return FIRST


def qnae_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('🕌 Qazo namozlarini ado etish 2-qism', callback_data='qnae_2')
        ],
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_n')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(QAZO_NAMOZLARINI_ADO_ETISH, reply_markup=reply_markup)
    return FIRST


# *********************************** qazo namozini ado etish tugashi ********************************************


# *********************************** e'tikor otirish boshlanishi ********************************************
def eo_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [

        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_n')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(ETIKOF_OTIRISH, reply_markup=reply_markup)
    return FIRST


# *********************************** e'tikor otirish tugashi ********************************************


# *********************************** tilovat sajdasi boshlanishi ********************************************
def tilovats_2_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tilovats')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TILOVAT_SAJDASI_2, reply_markup=reply_markup)
    return FIRST


def tilovats_3_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tilovats')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TILOVAT_SAJDASI_3, reply_markup=reply_markup)
    return FIRST


def tilovats_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('🕌 Tilovat sajdasi 2-qism', callback_data='tilovats_2'),
            InlineKeyboardButton('🕌 Tilovat sajdasi 3-qism', callback_data='tilovats_3')
        ],

        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_n')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TILOVAT_SAJDASI, reply_markup=reply_markup)
    return FIRST


# *********************************** tilovat sajdasi tugashi ********************************************


# *********************************** turli namozlar boshlanishi********************************************
def vitn_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(VITIR_NAMOZI, reply_markup=reply_markup)
    return FIRST


def tarovn_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TAROVEH_NAMOZI, reply_markup=reply_markup)
    return FIRST


def tarovn_2_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TAROVEH_NAMOZI_2, reply_markup=reply_markup)
    return FIRST


def musn_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(MUSOFIRNING_NAMOZI, reply_markup=reply_markup)
    return FIRST


def musn_2_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(MUSOFIRNING_NAMOZI_2, reply_markup=reply_markup)
    return FIRST


def juman_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(JUMA_NAMOZI, reply_markup=reply_markup)
    return FIRST


def juman_2_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(JUMA_NAMOZI_2, reply_markup=reply_markup)
    return FIRST


def juman_3_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(JUMA_NAMOZI_3, reply_markup=reply_markup)
    return FIRST


def janozan_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(JANOZA_NAMOZI, reply_markup=reply_markup)
    return FIRST


def janozan_2_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(JANOZA_NAMOZI_2, reply_markup=reply_markup)
    return FIRST


def janozan_3_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(JANOZA_NAMOZI_3, reply_markup=reply_markup)
    return FIRST


def janozan_4_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(JANOZA_NAMOZI_4, reply_markup=reply_markup)
    return FIRST


def janozan_5_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(JANOZA_NAMOZI_5, reply_markup=reply_markup)
    return FIRST


def iihn_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(IKKI_IYD_NAMOZI, reply_markup=reply_markup)
    return FIRST


def iihn_2_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(IKKI_IYD_NAMOZI_2, reply_markup=reply_markup)
    return FIRST


def iihn_3_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(IKKI_IYD_NAMOZI_3, reply_markup=reply_markup)
    return FIRST


def bkn_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(BEMOR_KISHINING_NAMOZI, reply_markup=reply_markup)
    return FIRST


def xn_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(XAVF_NAMOZI, reply_markup=reply_markup)
    return FIRST


def qvoton_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(QUYOSH_VA_OY_TUTILGANDAGI_NAMOZLAR, reply_markup=reply_markup)
    return FIRST


def istn_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(ISTIQO_NAMOZI, reply_markup=reply_markup)
    return FIRST


def nafln_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NAFL_NAMOZLAR, reply_markup=reply_markup)
    return FIRST


def nnot_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NAFL_NAMOZLARINI_OQISH_TARTIBIB, reply_markup=reply_markup)
    return FIRST


def nnot_2_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NAFL_NAMOZLARINI_OQISH_TARTIBIB_2, reply_markup=reply_markup)
    return FIRST


def shin_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(SHURUQ_NAMOZI, reply_markup=reply_markup)
    return FIRST


def zchn_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(ZUHO_NAMOZI, reply_markup=reply_markup)
    return FIRST


def shvn_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(SHUKRI_VUZU_NAMOZI, reply_markup=reply_markup)
    return FIRST


def istixn_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(ISTIHORA_NAMOZI, reply_markup=reply_markup)
    return FIRST


def hojn_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(HAJOAT_NAMOZI, reply_markup=reply_markup)
    return FIRST


def tavn_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TAVBA_NAMOZI, reply_markup=reply_markup)
    return FIRST


def avvn_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(AVOBBIYN_NAMOZI, reply_markup=reply_markup)
    return FIRST


def tahn_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TAHAJJUD_NAMOZI, reply_markup=reply_markup)
    return FIRST


def tasn_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TASBEH_NAMOZI, reply_markup=reply_markup)
    return FIRST


def tahiyyatulmn_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TAHIYYATUL_MASJID_NAMOZI, reply_markup=reply_markup)
    return FIRST


def markno_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_tn')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(MARKABDA_NAMOZ_OQISH, reply_markup=reply_markup)
    return FIRST


# *********************************** turli namozlar tugashi********************************************

def tn_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('🕌 Vitr namozi', callback_data='vitn'),
            InlineKeyboardButton('🕌 Taroveh namozi', callback_data='tarovn')
        ],
        [
            InlineKeyboardButton('🕌 Taroveh namozi 2-qism', callback_data='tarovn_2'),
            InlineKeyboardButton('🕌 Musofirning namozi', callback_data='musn'),
        ],
        [
            InlineKeyboardButton('🕌 Musofirning namozi 2-qism', callback_data='musn_2'),
            InlineKeyboardButton('🕌 Juma namozi', callback_data='juman')
        ],
        [
            InlineKeyboardButton('🕌 Juma namozi 2-qism', callback_data='juman_2'),
            InlineKeyboardButton('🕌 Juma namozi 3-qism', callback_data='juman_3'),
        ],
        [
            InlineKeyboardButton('🕌 Janoza namozi', callback_data='janozan'),
            InlineKeyboardButton('🕌 Janoza namozi 2-qism', callback_data='janozan_2')
        ],
        [
            InlineKeyboardButton('🕌 Janoza namozi 3-qism', callback_data='janozan_3'),
            InlineKeyboardButton('🕌 Janoza namozi 4-qism', callback_data='janozan_4')
        ],
        [
            InlineKeyboardButton('🕌 Janoza namozi 5-qism', callback_data='janozan_5'),
            InlineKeyboardButton('🕌 Ikki iyd(hayit) namozi', callback_data='iihn'),
        ],
        [
            InlineKeyboardButton('🕌 Ikki iyd(hayit) namozi 2-qism', callback_data='iihn_2'),
            InlineKeyboardButton('🕌 Ikki iyd(hayit) namozi 3-qism', callback_data='iihn_3')
        ],
        [
            InlineKeyboardButton('🕌 Bemor kishining namozi', callback_data='bkn'),
            InlineKeyboardButton('🕌 Xavf namozi', callback_data='xn')
        ],
        [
            InlineKeyboardButton('🕌 Quyosh va Oy tutilgandagi namozlar', callback_data='qvoton'),
            InlineKeyboardButton('🕌 Istisqo namozi', callback_data='istn')
        ],
        [
            InlineKeyboardButton('🕌 Nafl namozlar', callback_data='nafln'),
            InlineKeyboardButton('🕌 Markabda namoz o\'qish', callback_data='markno'),
        ],
        [
            InlineKeyboardButton('🕌 Shuruq (ishroq) namozi', callback_data='shin'),
            InlineKeyboardButton('🕌 Zuhro (choshgoh) namozi', callback_data='zchn')
        ],
        [
            InlineKeyboardButton('🕌 Shukri vuzu\' namozi', callback_data='shvn'),
            InlineKeyboardButton('🕌 Istixora namozi', callback_data='istixn')
        ],
        [
            InlineKeyboardButton('🕌 Hojat namozi', callback_data='hojn'),
            InlineKeyboardButton('🕌 Tavba namozi', callback_data='tavn')
        ],
        [
            InlineKeyboardButton('🕌 Avvobiyn namozi', callback_data='avvn'),
            InlineKeyboardButton('🕌 Tahajjud namozi', callback_data='tahn')
        ],
        [
            InlineKeyboardButton('🕌 Tasbeh namozi', callback_data='tasn'),
            InlineKeyboardButton('🕌 Tahiyyatul masjid namozi', callback_data='tahiyyatulmn')
        ],
        [
            InlineKeyboardButton('🕌 Nafl namozlarini o\'qish taritibi', callback_data='nnot'),
            InlineKeyboardButton('🕌 Nafl namozlarini o\'qish taritibi 2-qism', callback_data='nnot_2')
        ],
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_n')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TURLI_NAMOZLAR, reply_markup=reply_markup)
    return FIRST


def two(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('🕌 Namozga poklanish', callback_data='np'),
            InlineKeyboardButton('🕌 G\'usul', callback_data='gusul'),
        ],
        [
            InlineKeyboardButton('🕌 Tahorat', callback_data='tahorat'),
            InlineKeyboardButton('🕌 Tayammum', callback_data='tayammum'),
        ],
        [
            InlineKeyboardButton('🕌 Namoz', callback_data='namoz'),
            InlineKeyboardButton('🕌 Namozda o\'qiladigan kichik suralar va duolar', callback_data='noksvd'),
        ],
        [
            InlineKeyboardButton('🕌 Namozdan so\'ng o\'qiladigan duolar', callback_data='nsod'),
            InlineKeyboardButton('🕌 Jamoat namozi', callback_data='jn'),
        ],
        [
            InlineKeyboardButton('🕌 Ibratli namozlar', callback_data='in'),
            InlineKeyboardButton('🕌 Qazo namozlarini ado edish', callback_data='qnae'),
        ],
        [
            InlineKeyboardButton('🕌 Turli namozlar', callback_data='tn'),
            InlineKeyboardButton('🕌 E\'tikof o\'tirish', callback_data='eo'),
        ],
        [
            InlineKeyboardButton('🕌 Tilovat sajdasi', callback_data='tilovats'),

        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(
        '🕌 NAMOZ DARSLARI\n\n📖 Shayx Muhammad Sodiq Muhammad Yusuf xazratlarining \"Mo\'mining me\'roji\" nomli kitobi asosida tayyorlandi.',
        reply_markup=reply_markup)
    return FIRST


# ************************************************ zakot nima boshlanishi***********************************************************
def zakn_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_three')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(ZAKOT_NIMA, reply_markup=reply_markup)
    return FIRST


def zakfx_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_three')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(ZAKOTNING_FIQHIY_HUKUMLARI, reply_markup=reply_markup)
    return FIRST


def chhz_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_three')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(CHORVA_HAYVONLARNING_HUKUMLARI, reply_markup=reply_markup)
    return FIRST


def tvkz_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_three')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TILLA_VAKUMUSHNING_ZAKOTI, reply_markup=reply_markup)
    return FIRST


def npoz_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_three')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(NAQT_PULDAN_OLINADIGAN_ZAKOT, reply_markup=reply_markup)
    return FIRST


def tmqza_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_three')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TIJORAT_MOLIDAN_OLNADIGAN_ZAKOT, reply_markup=reply_markup)
    return FIRST


def tkbz_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_three')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TILLA_VAKUMUSHNING_ZAKOTI, reply_markup=reply_markup)
    return FIRST


def qtz_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_three')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(QIMMATBAHO_TOSHLARNING_ZAKOTI, reply_markup=reply_markup)
    return FIRST


def zomb_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_three')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(ZAKOT_OLISHI_MUMKIN_BOLMAGANLAR, reply_markup=reply_markup)
    return FIRST


def zbv_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_three')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(ZAKOT_BERUVCHILARNING_VAZIFALARI, reply_markup=reply_markup)
    return FIRST


# ************************************************ zakot nima tugashi***********************************************************

# ************************************************ three start ***********************************************************
def three(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('💰 Zakot nima?', callback_data='zakn'),
            InlineKeyboardButton('💰 Zakotning fiqxiy xukumlari', callback_data='zakfx'),
        ],
        [
            InlineKeyboardButton('💰 Chorva Hayvonlarning zakotlari', callback_data='chhz'),
            InlineKeyboardButton('💰 Tilla va kumish zakoti', callback_data='tvkz'),
        ],
        [
            InlineKeyboardButton('💰 Naqd puldan olinadigan zakot', callback_data='npoz'),
            InlineKeyboardButton('💰 Tijorat molidan qiymatini zakotga chiqarish', callback_data='tmqza'),
        ],
        [
            InlineKeyboardButton('💰 Tilla-kumish buyumlar, idishlar va taqinchoqlarning zakoti', callback_data='tkbz'),
            InlineKeyboardButton('💰 Qimmatbaho toshlarning zakoti', callback_data='qtz'),
        ],
        [
            InlineKeyboardButton('💰 Zakot olishi mumkin bo\'maganlar', callback_data='zomb'),
            InlineKeyboardButton('💰 Zakot beruvchilarning vazifalari', callback_data='zbv'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh')
        ]

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(
        '💰 ZAKOT DARSLARI\n\n📖 Shayx Muhammad Sodiq Muhammad Yusuf xazratlarining \"Mo\'mining me\'roji\" nomli kitobi asosida tayyorlandi.',
        reply_markup=reply_markup)
    return FIRST


# ************************************************ three end ***********************************************************


# ************************************************ roza start ***********************************************************
def rqi_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_four')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(ROZA_QANDAY_IBODAT, reply_markup=reply_markup)
    return FIRST


def rd_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_four')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(ROZANING_DARAJALARI, reply_markup=reply_markup)
    return FIRST


def rsh_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_four')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(ROZANING_SHARTLARI, reply_markup=reply_markup)
    return FIRST


def rt_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_four')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(ROZANING_TURLARI, reply_markup=reply_markup)
    return FIRST


def rthbk_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_four')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(ROZANI_TUTISH_HAROM_BOLGAN_KUNLAR, reply_markup=reply_markup)
    return FIRST


def rn_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_four')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(ROZANING_NIYATLARI, reply_markup=reply_markup)
    return FIRST


def svi_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_four')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(SAHARLIK_VA_IFTORLIK, reply_markup=reply_markup)
    return FIRST


def rtmbk_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_four')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(ROZANI_TUTISH_MAKRUH_BOLGAN_KUNLAR, reply_markup=reply_markup)
    return FIRST


def rm_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_four')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(ROZANING_MUSTAHABLARI, reply_markup=reply_markup)
    return FIRST


def rbn_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_four')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(ROZANI_BUZADIGAN_NARSALAR, reply_markup=reply_markup)
    return FIRST


def rbn_2_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_four')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(ROZANI_BUZADIGAN_NARSALAR_2, reply_markup=reply_markup)
    return FIRST


# ************************************************ roza end ***********************************************************
def four(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('🤲🏻 Ro\'za qanday ibodat?', callback_data='rqi'),
            InlineKeyboardButton('🤲🏻 Ro\'zaning darajalari', callback_data='rd'),
        ],
        [
            InlineKeyboardButton('🤲🏻 Ro\'zaning shartlari', callback_data='rsh'),
            InlineKeyboardButton('🤲🏻 Ro\'zaning turlari', callback_data='rt'),
        ],
        [
            InlineKeyboardButton('🤲🏻 Ro\'za tutish harom bo\'lgan kunlar', callback_data='rthbk'),
            InlineKeyboardButton('🤲🏻 Ro\'zaning niyati', callback_data='rn'),
        ],
        [
            InlineKeyboardButton('🤲🏻 Saharlik va Iftorlik', callback_data='svi'),
            InlineKeyboardButton('🤲🏻 Ro\'za tutish makruh bo\'lgan kunlar', callback_data='rtmbk'),
        ],
        [
            InlineKeyboardButton('🤲🏻 Ro\'zaning mustahablari', callback_data='rm'),
            InlineKeyboardButton('🤲🏻 Ro\'zani buzadigan narsalar', callback_data='rbn'),
        ],
        [
            InlineKeyboardButton('🤲🏻 Ro\'zani buzadigan narsalar 2-qism', callback_data='rbn_2'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh')
        ]

    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(
        '🤲🏻  RO\'ZA DARSLARI\n\n📖 Shayx Muhammad Sodiq Muhammad Yusuf xazratlarining \"Mo\'mining me\'roji\" nomli kitobi asosida tayyorlandi.',
        reply_markup=reply_markup)
    return FIRST


# ************************************************ three end ***********************************************************
# ************************************************ five end ***********************************************************
def hqi_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_five')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(HAJ_QANDAY_IBODAT, reply_markup=reply_markup)
    return FIRST


def ho_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_five')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(HAJNING_ODOBLARI, reply_markup=reply_markup)
    return FIRST


def hscht_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_five')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(HAJ_SAFARIGA_CHIQUVCHILARGA_TAVSIYALAR, reply_markup=reply_markup)
    return FIRST


def hit_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_five')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(HAJ_IBODATI_TURLARI, reply_markup=reply_markup)
    return FIRST


def hit_2_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_five')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(HAJ_IBODATI_TURLARI_2, reply_markup=reply_markup)
    return FIRST


def hfvvs_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_five')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(HAJNING_FAPZ_VA_VOJIB_SUNNATLARI, reply_markup=reply_markup)
    return FIRST


def ek_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_five')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(EHROMGA_KIRISH, reply_markup=reply_markup)
    return FIRST


def eavuk_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_five')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(EHROMDAGI_AMALLAR_VA_UNING_KAFFORATLARI, reply_markup=reply_markup)
    return FIRST


def eavuk_2_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_five')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(EHROMDAGI_AMALLAR_VA_UNING_KAFFORATLARI_2, reply_markup=reply_markup)
    return FIRST


def eavuk_3_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_five')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(EHROMDAGI_AMALLAR_VA_UNING_KAFFORATLARI_3, reply_markup=reply_markup)
    return FIRST


def ta_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_five')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TALBIYA_AYTISH, reply_markup=reply_markup)
    return FIRST


def xshk_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_five')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(HARAMI_SHAROFGA_KIRISH, reply_markup=reply_markup)
    return FIRST


def tb_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_five')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TAVOFNI_BOSHLASH, reply_markup=reply_markup)
    return FIRST


def svmosq_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_five')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(SAFO_VA_MARVA_QILISH_ORASIDA_SAY_QILISH, reply_markup=reply_markup)
    return FIRST


def mt_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_five')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(MINODA_TURISH, reply_markup=reply_markup)
    return FIRST


def at_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_five')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(AROFATDA_TURISH, reply_markup=reply_markup)
    return FIRST


def at_2_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_five')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(AROFATDA_TURISH_2, reply_markup=reply_markup)
    return FIRST


def mb_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_five')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(MUZDALIFADA_BOLISH, reply_markup=reply_markup)
    return FIRST


def shto_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_five')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(SHAYTONGA_TOSH_OTISH, reply_markup=reply_markup)
    return FIRST


def shto_2_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_five')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(SHAYTONGA_TOSH_OTISH_2, reply_markup=reply_markup)
    return FIRST


def tt_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_five')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(TAVOFNING_TURLARI, reply_markup=reply_markup)
    return FIRST


def hbk_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_five')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(HAJNING_BESH_KUNI, reply_markup=reply_markup)
    return FIRST


def hbk_2_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_five')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(HAJNING_BESH_KUNI_2, reply_markup=reply_markup)
    return FIRST


def bhaji_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_five')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(BADAL_HAJI, reply_markup=reply_markup)
    return FIRST


def hns_f(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('➡️ Orqaga qaytish', callback_data='back_five')
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data="bh")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(HAJNING_NOZIK_SIRLARI, reply_markup=reply_markup)
    return FIRST


# ************************************************ five end ***********************************************************

def five(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    buttons = [
        [
            InlineKeyboardButton('🕋 Haj qanday ibodat', callback_data='hqi'),
            InlineKeyboardButton('🕋 Hajning odoblari', callback_data='ho'),
        ],
        [
            InlineKeyboardButton('🕋 Haj safariga chiquvchilarga tavsiyalar', callback_data='hscht'),
            InlineKeyboardButton('🕋 Talbiya aytish', callback_data='ta'),
        ],

        [
            InlineKeyboardButton('🕋 Hajning farz, vojib va sunnatlari', callback_data='hfvvs'),
            InlineKeyboardButton('🕋 Ehromga kirish', callback_data='ek'),
        ],
        [

            InlineKeyboardButton('🕋 Arofatda turish', callback_data='at'),
            InlineKeyboardButton('🕋 Arofatda turish 2-qism', callback_data='at_2'),

        ],
        [
            InlineKeyboardButton('🕋 Xarami sharifga kirish', callback_data='xshk'),
            InlineKeyboardButton('🕋 Tavofni boshlash', callback_data='tb'),
        ],
        [
            InlineKeyboardButton('🕋 Safo va marva orasida sa\'y qilish', callback_data='svmosq'),
            InlineKeyboardButton('🕋 Minoda turish', callback_data='mt'),
        ],
        [
            InlineKeyboardButton('🕋 Muzdalifada bo\'lish', callback_data='mb'),
            InlineKeyboardButton('🕋 Tavofning turlari', callback_data='tt'),
        ],
        [
            InlineKeyboardButton('🕋 Shaytonga tosh otish', callback_data='shto'),
            InlineKeyboardButton('🕋 Shaytonga tosh otish 2-qism', callback_data='shto_2'),
        ],
        [
            InlineKeyboardButton('🕋 Hajning besh kuni', callback_data='hbk'),
            InlineKeyboardButton('🕋 Hajning besh kuni 2-qism', callback_data='hbk_2'),
        ],
        [
            InlineKeyboardButton('🕋 Haj ibodati turlari', callback_data='hit'),
            InlineKeyboardButton('🕋 Haj ibodati turlari 2-qism', callback_data='hit_2'),
        ],
        [
            InlineKeyboardButton('🕋 Badal Haji', callback_data='bhaji'),
            InlineKeyboardButton('🕋 Hajning nozik sirlari', callback_data='hns'),
        ],
        [
            InlineKeyboardButton('🕋 Ehromdagi amallar va ularning kafforatlari', callback_data='eavuk'),
            InlineKeyboardButton('🕋 Ehromdagi amallar va ularning kafforatlari 2-qism', callback_data='eavuk_2'),
        ],
        [
            InlineKeyboardButton('🕋 Ehromdagi amallar va ularning kafforatlari 3-qism', callback_data='eavuk_3'),
        ],
        [
            InlineKeyboardButton('🔄 Boshiga qaytish', callback_data='bh')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text(
        '🕋 HAJ DARSLARI\n\n📖 Shayx Muhammad Sodiq Muhammad Yusuf xazratlarining \"Mo\'mining me\'roji\" nomli kitobi asosida tayyorlandi.',
        reply_markup=reply_markup)
    return FIRST


# ************************************************ five end ***********************************************************

def main():
    updater = Updater(TOKEN, use_context=True)
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', hello)],

        states={
            FIRST: [
                CallbackQueryHandler(one, pattern='^' + 'Iymon' + '$'),
                CallbackQueryHandler(two, pattern='^' + 'Namoz' + '$'),
                CallbackQueryHandler(three, pattern='^' + 'Zakot' + '$'),
                CallbackQueryHandler(four, pattern='^' + 'Ro\'za' + '$'),
                CallbackQueryHandler(five, pattern='^' + 'Haj' + '$'),
                CallbackQueryHandler(dvsh, pattern='^' + 'dvsh' + '$'),
                CallbackQueryHandler(iyn, pattern='^' + 'iyn' + '$'),
                CallbackQueryHandler(ati, pattern='^' + 'ati' + '$'),
                CallbackQueryHandler(fi, pattern='^' + 'fi' + '$'),
                CallbackQueryHandler(iki, pattern='^' + 'iki' + '$'),
                CallbackQueryHandler(pi, pattern='^' + 'pi' + '$'),
                CallbackQueryHandler(oki, pattern='^' + 'oki' + '$'),
                CallbackQueryHandler(qi, pattern='^' + 'qi' + '$'),
                CallbackQueryHandler(osi, pattern='^' + 'osi' + '$'),
                CallbackQueryHandler(aqida, pattern='^' + 'aqida' + '$'),
                CallbackQueryHandler(asvj, pattern='^' + 'asvj' + '$'),
                CallbackQueryHandler(hah, pattern='^' + 'hah' + '$'),
                CallbackQueryHandler(hello_over, pattern='^' + 'bh' + '$'),
                CallbackQueryHandler(one, pattern='^' + 'back' + '$'),
                CallbackQueryHandler(np_f, pattern='^' + 'np' + '$'),
                CallbackQueryHandler(gusul_f, pattern='^' + 'gusul' + '$'),
                CallbackQueryHandler(qhgq_f, pattern='^' + 'qhgq' + '$'),
                CallbackQueryHandler(gqfbh_f, pattern='^' + 'gqfbh' + '$'),
                CallbackQueryHandler(gh_f, pattern='^' + 'gh' + '$'),
                CallbackQueryHandler(gqsbh_f, pattern='^' + 'gqsbh' + '$'),
                CallbackQueryHandler(gqmbh_f, pattern='^' + 'gqmbh' + '$'),
                CallbackQueryHandler(gfvs_f, pattern='^' + 'gfvs' + '$'),
                CallbackQueryHandler(tahorat_f, pattern='^' + 'tahorat' + '$'),
                CallbackQueryHandler(taxsh_f, pattern='^' + 'taxsh' + '$'),
                CallbackQueryHandler(shitiqb_f, pattern='^' + 'shitiqb' + '$'),
                CallbackQueryHandler(taxsn_f, pattern='^' + 'taxsn' + '$'),
                CallbackQueryHandler(taxm_f, pattern='^' + 'taxm' + '$'),
                CallbackQueryHandler(taxo_f, pattern='^' + 'taxo' + '$'),
                CallbackQueryHandler(taxs_f, pattern='^' + 'taxs' + '$'),
                CallbackQueryHandler(taxf_f, pattern='^' + 'taxf' + '$'),
                CallbackQueryHandler(tahorat_f, pattern='^' + 'back_t' + '$'),
                CallbackQueryHandler(tayammum_f, pattern='^' + 'tayammum' + '$'),
                CallbackQueryHandler(tsh_f, pattern='^' + 'tsh' + '$'),
                CallbackQueryHandler(tr_f, pattern='^' + 'tr' + '$'),
                CallbackQueryHandler(tqt_f, pattern='^' + 'tqt' + '$'),
                CallbackQueryHandler(tf_f, pattern='^' + 'tf' + '$'),
                CallbackQueryHandler(ts_f, pattern='^' + 'ts' + '$'),
                CallbackQueryHandler(tbn_f, pattern='^' + 'tbn' + '$'),
                CallbackQueryHandler(tayammum_f, pattern='^' + 'back_tay' + '$'),
                CallbackQueryHandler(namoz_f, pattern='^' + 'namoz' + '$'),
                CallbackQueryHandler(namoz_2_f, pattern='^' + 'namoz_2' + '$'),
                CallbackQueryHandler(ah_f, pattern='^' + 'ah' + '$'),
                CallbackQueryHandler(nh_f, pattern='^' + 'nh' + '$'),
                CallbackQueryHandler(nh_2_f, pattern='^' + 'nh_2' + '$'),
                CallbackQueryHandler(nt_f, pattern='^' + 'nt' + '$'),
                CallbackQueryHandler(nv_f, pattern='^' + 'nv' + '$'),
                CallbackQueryHandler(nr_f, pattern='^' + 'nr' + '$'),
                CallbackQueryHandler(avi_f, pattern='^' + 'avi' + '$'),
                CallbackQueryHandler(irfnot_f, pattern='^' + 'irfnot' + '$'),
                CallbackQueryHandler(trfnot_f, pattern='^' + 'trfnot' + '$'),
                CallbackQueryHandler(urfnot_f, pattern='^' + 'urfnot' + '$'),
                CallbackQueryHandler(ss_f, pattern='^' + 'ss' + '$'),
                CallbackQueryHandler(ss_2_f, pattern='^' + 'ss_2' + '$'),
                CallbackQueryHandler(ss_3_f, pattern='^' + 'ss_3' + '$'),
                CallbackQueryHandler(ss_4_f, pattern='^' + 'ss_4' + '$'),
                CallbackQueryHandler(sutra_f, pattern='^' + 'sutra' + '$'),
                CallbackQueryHandler(nvojib_f, pattern='^' + 'nvojib' + '$'),
                CallbackQueryHandler(ns_f, pattern='^' + 'ns' + '$'),
                CallbackQueryHandler(nm_f, pattern='^' + 'nm' + '$'),
                CallbackQueryHandler(nha_f, pattern='^' + 'nha' + '$'),
                CallbackQueryHandler(nmrea_f, pattern='^' + 'nmrea' + '$'),
                CallbackQueryHandler(ah_f, pattern='^' + 'ah' + '$'),
                CallbackQueryHandler(nma_f, pattern='^' + 'nma' + '$'),
                CallbackQueryHandler(nbamallar_f, pattern='^' + 'nbamallar' + '$'),
                CallbackQueryHandler(no_f, pattern='^' + 'no' + '$'),
                CallbackQueryHandler(qibla_f, pattern='^' + 'qibla' + '$'),
                CallbackQueryHandler(mba_f, pattern='^' + 'mba' + '$'),
                CallbackQueryHandler(nbf_f, pattern='^' + 'nbf' + '$'),
                CallbackQueryHandler(nbf_2_f, pattern='^' + 'nbf_2' + '$'),
                CallbackQueryHandler(trsnot_f, pattern='^' + 'trsnot' + '$'),
                CallbackQueryHandler(nfa_f, pattern='^' + 'nfa' + '$'),
                CallbackQueryHandler(namoz_f, pattern='^' + 'back_namoz' + '$'),

                CallbackQueryHandler(noksvd_f, pattern='^' + 'noksvd' + '$'),
                CallbackQueryHandler(fos_f, pattern='^' + 'fos' + '$'),
                CallbackQueryHandler(fis_f, pattern='^' + 'fis' + '$'),
                CallbackQueryHandler(qus_f, pattern='^' + 'qus' + '$'),
                CallbackQueryHandler(mas_f, pattern='^' + 'mas' + '$'),
                CallbackQueryHandler(kas_f, pattern='^' + 'kas' + '$'),
                CallbackQueryHandler(kafs_f, pattern='^' + 'kafs' + '$'),
                CallbackQueryHandler(nas_f, pattern='^' + 'nas' + '$'),
                CallbackQueryHandler(maqs_f, pattern='^' + 'maqs' + '$'),
                CallbackQueryHandler(fals_f, pattern='^' + 'fals' + '$'),
                CallbackQueryHandler(ans_f, pattern='^' + 'ans' + '$'),
                CallbackQueryHandler(ixs_f, pattern='^' + 'ixs' + '$'),
                CallbackQueryHandler(sano_f, pattern='^' + 'sano' + '$'),
                CallbackQueryHandler(tashahhud_f, pattern='^' + 'tashahhud' + '$'),
                CallbackQueryHandler(salovat_f, pattern='^' + 'salovat' + '$'),
                CallbackQueryHandler(qud_f, pattern='^' + 'qud' + '$'),
                CallbackQueryHandler(kook_f, pattern='^' + 'kook' + '$'),

                CallbackQueryHandler(jn_f, pattern='^' + 'jn' + '$'),
                CallbackQueryHandler(jn_2_f, pattern='^' + 'jn_2' + '$'),
                CallbackQueryHandler(jn_3_f, pattern='^' + 'jn_3' + '$'),
                CallbackQueryHandler(nst_f, pattern='^' + 'nst' + '$'),
                CallbackQueryHandler(imkl_f, pattern='^' + 'imkl' + '$'),
                CallbackQueryHandler(masodob_f, pattern='^' + 'masodob' + '$'),
                CallbackQueryHandler(masodob_2_f, pattern='^' + 'masodob_2' + '$'),
                CallbackQueryHandler(masodob_3_f, pattern='^' + 'masodob_3' + '$'),
                CallbackQueryHandler(masodob_4_f, pattern='^' + 'masodob_4' + '$'),
                CallbackQueryHandler(masodob_5_f, pattern='^' + 'masodob_5' + '$'),

                CallbackQueryHandler(in_f, pattern='^' + 'in' + '$'),
                CallbackQueryHandler(in_2_f, pattern='^' + 'in_2' + '$'),
                CallbackQueryHandler(avan_f, pattern='^' + 'avan' + '$'),
                CallbackQueryHandler(svtn_f, pattern='^' + 'svtn' + '$'),
                CallbackQueryHandler(svtn_2_f, pattern='^' + 'svtn_2' + '$'),
                CallbackQueryHandler(rxn_f, pattern='^' + 'rxn' + '$'),

                CallbackQueryHandler(qnae_f, pattern='^' + 'qnae' + '$'),
                CallbackQueryHandler(qnae_2_f, pattern='^' + 'qnae_2' + '$'),
                CallbackQueryHandler(eo_f, pattern='^' + 'eo' + '$'),

                CallbackQueryHandler(tilovats_f, pattern='^' + 'tilovats' + '$'),
                CallbackQueryHandler(tilovats_2_f, pattern='^' + 'tilovats_2' + '$'),
                CallbackQueryHandler(tilovats_3_f, pattern='^' + 'tilovats_3' + '$'),

                CallbackQueryHandler(tn_f, pattern='^' + 'tn' + '$'),
                CallbackQueryHandler(vitn_f, pattern='^' + 'vitn' + '$'),
                CallbackQueryHandler(tarovn_f, pattern='^' + 'tarovn' + '$'),
                CallbackQueryHandler(tarovn_2_f, pattern='^' + 'tarovn_2' + '$'),
                CallbackQueryHandler(musn_f, pattern='^' + 'musn' + '$'),
                CallbackQueryHandler(musn_2_f, pattern='^' + 'musn_2' + '$'),
                CallbackQueryHandler(juman_f, pattern='^' + 'juman' + '$'),
                CallbackQueryHandler(juman_2_f, pattern='^' + 'juman_2' + '$'),
                CallbackQueryHandler(juman_3_f, pattern='^' + 'juman_3' + '$'),
                CallbackQueryHandler(janozan_f, pattern='^' + 'janozan' + '$'),
                CallbackQueryHandler(janozan_2_f, pattern='^' + 'janozan_2' + '$'),
                CallbackQueryHandler(janozan_3_f, pattern='^' + 'janozan_3' + '$'),
                CallbackQueryHandler(janozan_4_f, pattern='^' + 'janozan_4' + '$'),
                CallbackQueryHandler(janozan_5_f, pattern='^' + 'janozan_5' + '$'),
                CallbackQueryHandler(iihn_f, pattern='^' + 'iihn' + '$'),
                CallbackQueryHandler(iihn_2_f, pattern='^' + 'iihn_2' + '$'),
                CallbackQueryHandler(iihn_3_f, pattern='^' + 'iihn_3' + '$'),
                CallbackQueryHandler(bkn_f, pattern='^' + 'bkn' + '$'),
                CallbackQueryHandler(xn_f, pattern='^' + 'xn' + '$'),
                CallbackQueryHandler(qvoton_f, pattern='^' + 'qvoton' + '$'),
                CallbackQueryHandler(istn_f, pattern='^' + 'istn' + '$'),
                CallbackQueryHandler(nafln_f, pattern='^' + 'nafln' + '$'),
                CallbackQueryHandler(nnot_f, pattern='^' + 'nnot' + '$'),
                CallbackQueryHandler(nnot_2_f, pattern='^' + 'nnot_2' + '$'),
                CallbackQueryHandler(shin_f, pattern='^' + 'shin' + '$'),
                CallbackQueryHandler(zchn_f, pattern='^' + 'zchn' + '$'),
                CallbackQueryHandler(shvn_f, pattern='^' + 'shvn' + '$'),
                CallbackQueryHandler(istixn_f, pattern='^' + 'istixn' + '$'),
                CallbackQueryHandler(hojn_f, pattern='^' + 'hojn' + '$'),
                CallbackQueryHandler(tavn_f, pattern='^' + 'tavn' + '$'),
                CallbackQueryHandler(avvn_f, pattern='^' + 'avvn' + '$'),
                CallbackQueryHandler(tahn_f, pattern='^' + 'tahn' + '$'),
                CallbackQueryHandler(tasn_f, pattern='^' + 'tasn' + '$'),
                CallbackQueryHandler(tahiyyatulmn_f, pattern='^' + 'tahiyyatulmn' + '$'),
                CallbackQueryHandler(markno_f, pattern='^' + 'markno' + '$'),

                CallbackQueryHandler(zakn_f, pattern='^' + 'zakn' + '$'),
                CallbackQueryHandler(zakfx_f, pattern='^' + 'zakfx' + '$'),
                CallbackQueryHandler(chhz_f, pattern='^' + 'chhz' + '$'),
                CallbackQueryHandler(tvkz_f, pattern='^' + 'tvkz' + '$'),
                CallbackQueryHandler(npoz_f, pattern='^' + 'npoz' + '$'),
                CallbackQueryHandler(tmqza_f, pattern='^' + 'tmqza' + '$'),
                CallbackQueryHandler(tkbz_f, pattern='^' + 'tkbz' + '$'),
                CallbackQueryHandler(qtz_f, pattern='^' + 'qtz' + '$'),
                CallbackQueryHandler(zomb_f, pattern='^' + 'zomb' + '$'),
                CallbackQueryHandler(zbv_f, pattern='^' + 'zbv' + '$'),
                CallbackQueryHandler(three, pattern='^' + 'back_three' + '$'),

                CallbackQueryHandler(rqi_f, pattern='^' + 'rqi' + '$'),
                CallbackQueryHandler(rd_f, pattern='^' + 'rd' + '$'),
                CallbackQueryHandler(rsh_f, pattern='^' + 'rsh' + '$'),
                CallbackQueryHandler(rt_f, pattern='^' + 'rt' + '$'),
                CallbackQueryHandler(rthbk_f, pattern='^' + 'rthbk' + '$'),
                CallbackQueryHandler(rn_f, pattern='^' + 'rn' + '$'),
                CallbackQueryHandler(svi_f, pattern='^' + 'svi' + '$'),
                CallbackQueryHandler(rtmbk_f, pattern='^' + 'rtmbk' + '$'),
                CallbackQueryHandler(rm_f, pattern='^' + 'rm' + '$'),
                CallbackQueryHandler(rbn_f, pattern='^' + 'rbn' + '$'),
                CallbackQueryHandler(rbn_2_f, pattern='^' + 'rbn_2' + '$'),
                CallbackQueryHandler(four, pattern='^' + 'back_four' + '$'),

                CallbackQueryHandler(hqi_f, pattern='^' + 'hqi' + '$'),
                CallbackQueryHandler(ho_f, pattern='^' + 'ho' + '$'),
                CallbackQueryHandler(hscht_f, pattern='^' + 'hscht' + '$'),
                CallbackQueryHandler(hit_f, pattern='^' + 'hit' + '$'),
                CallbackQueryHandler(hit_2_f, pattern='^' + 'hit_2' + '$'),
                CallbackQueryHandler(hfvvs_f, pattern='^' + 'hfvvs' + '$'),
                CallbackQueryHandler(ek_f, pattern='^' + 'ek' + '$'),
                CallbackQueryHandler(eavuk_f, pattern='^' + 'eavuk' + '$'),
                CallbackQueryHandler(eavuk_2_f, pattern='^' + 'eavuk_2' + '$'),
                CallbackQueryHandler(eavuk_3_f, pattern='^' + 'eavuk_3' + '$'),
                CallbackQueryHandler(ta_f, pattern='^' + 'ta' + '$'),
                CallbackQueryHandler(xshk_f, pattern='^' + 'xshk' + '$'),
                CallbackQueryHandler(tb_f, pattern='^' + 'tb' + '$'),
                CallbackQueryHandler(svmosq_f, pattern='^' + 'svmosq' + '$'),
                CallbackQueryHandler(mt_f, pattern='^' + 'mt' + '$'),
                CallbackQueryHandler(at_f, pattern='^' + 'at' + '$'),
                CallbackQueryHandler(at_2_f, pattern='^' + 'at_2' + '$'),
                CallbackQueryHandler(mb_f, pattern='^' + 'mb' + '$'),
                CallbackQueryHandler(shto_f, pattern='^' + 'shto' + '$'),
                CallbackQueryHandler(shto_2_f, pattern='^' + 'shto_2' + '$'),
                CallbackQueryHandler(tt_f, pattern='^' + 'tt' + '$'),
                CallbackQueryHandler(hbk_f, pattern='^' + 'hbk' + '$'),
                CallbackQueryHandler(hbk_2_f, pattern='^' + 'hbk_2' + '$'),
                CallbackQueryHandler(bhaji_f, pattern='^' + 'bhaji' + '$'),
                CallbackQueryHandler(hns_f, pattern='^' + 'hns' + '$'),
                CallbackQueryHandler(five, pattern='^' + 'back_five' + '$'),

                CallbackQueryHandler(tn_f, pattern='^' + 'back_tn' + '$'),
                CallbackQueryHandler(tilovats_f, pattern='^' + 'back_tilovats' + '$'),
                CallbackQueryHandler(qnae_f, pattern='^' + 'back_qnae' + '$'),
                CallbackQueryHandler(in_f, pattern='^' + 'back_in' + '$'),
                CallbackQueryHandler(jn_f, pattern='^' + 'back_jn' + '$'),
                CallbackQueryHandler(noksvd_f, pattern='^' + 'back_noksvd' + '$'),
                CallbackQueryHandler(nsod_f, pattern='^' + 'nsod' + '$'),
                CallbackQueryHandler(two, pattern='^' + 'back_n' + '$'),
                CallbackQueryHandler(gusul_f, pattern='^' + 'back_m' + '$'),
            ],
            SECOND: [
                CallbackQueryHandler(one, pattern='^' + 'back' + '$'),

            ],

        },
        fallbacks=[CommandHandler('start', hello)]
    )
    updater.dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()