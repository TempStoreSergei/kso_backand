#ifndef C_CLASSIC_API_H
#define C_CLASSIC_API_H
#include <cstdbool>
#include <cstddef>
#include <cstdint>
#include <ctime>

#if defined _WIN32 || defined __CYGWIN__
#define C_CLASSIC_FR_DRV_NGX_HELPER_DLL_IMPORT __declspec(dllimport)
#define C_CLASSIC_FR_DRV_NGX_HELPER_DLL_EXPORT __declspec(dllexport)
#define C_CLASSIC_FR_DRV_NGX_HELPER_DLL_LOCAL
#else
#if __GNUC__ >= 4
#define C_CLASSIC_FR_DRV_NGX_HELPER_DLL_IMPORT __attribute__((visibility("default")))
#define C_CLASSIC_FR_DRV_NGX_HELPER_DLL_EXPORT __attribute__((visibility("default")))
#define C_CLASSIC_FR_DRV_NGX_HELPER_DLL_LOCAL __attribute__((visibility("hidden")))
#else
#define C_CLASSIC_FR_DRV_NGX_HELPER_DLL_IMPORT
#define C_CLASSIC_FR_DRV_NGX_HELPER_DLL_EXPORT
#define C_CLASSIC_FR_DRV_NGX_HELPER_DLL_LOCAL
#endif
#endif
#ifdef C_CLASSIC_FR_DRV_NGX_DLL
#ifdef C_CLASSIC_FR_DRV_NGX_DLL_EXPORTS
#define C_CLASSIC_FR_DRV_NGX_API C_CLASSIC_FR_DRV_NGX_HELPER_DLL_EXPORT
#else
#define C_CLASSIC_FR_DRV_NGX_API C_CLASSIC_FR_DRV_NGX_HELPER_DLL_IMPORT
#endif
#define C_CLASSIC_FR_DRV_NGX_LOCAL C_CLASSIC_FR_DRV_NGX_HELPER_DLL_LOCAL
#else
#define C_CLASSIC_FR_DRV_NGX_API
#define C_CLASSIC_FR_DRV_NGX_LOCAL
#endif

namespace kkt_driver {

#ifdef __cplusplus
extern "C" {
#endif

enum TBarcodeAlignment {
    baCenter = 0,
    baLeft = 1,
    baRight = 2,
};
enum TFinishDocumentMode {
    fdmTrailerDisabled = 0,
    fdmTrailerEnabled = 1,
};
enum TBinaryConversion {
    BINARY_CONVERSION_NONE = 0,
    BINARY_CONVERSION_HEX = 1,
};
enum TCodePage {
    CODE_PAGE_DEFAULT = 0,
    CODE_PAGE_RUSSIAN = 1,
    CODE_PAGE_ARMENIAN_UNICODE = 2,
    CODE_PAGE_ARMENIAN_ANSI = 3,
    CODE_PAGE_KAZAKH_UNICODE = 4,
    CODE_PAGE_TURKMEN_UNICODE = 5,
};
enum TConnectionType {
    Local = 0,
    ServerTcp = 1,
    ServerDCOM = 2,
    ESCAPE = 3,
    NotUsed = 4,
    Emulator = 5,
    Tcp = 6,
};
enum BarcodeTextPosition {
    BCT_None = 0,
    BCT_Below = 1,
    BCT_Above = 2,
    BCT_Both = 3,
};
enum BarcodeLineType {
    BC1D_Code128A,
    BC1D_Code128B,
    BC1D_Code128C,
    BC1D_ReservedForQR,
    BC1D_Code39,
    BC1D_EAN13,
};
enum Barcode2DType {
    BC2D_PDF417,
    BC2D_DATAMATRIX,
    BC2D_AZTEC,
    BC2D_QRCODE,
};
enum DevicePropertiesEnumeration {
    DPE_f00_journal_weight_sensor = 0,
    DPE_f01_receipt_weight_sensor,
    DPE_f02_journal_opt_sensor,
    DPE_f03_receipt_opt_sensor,
    DPE_f04_cover_sensor,
    DPE_f05_journal_lever,
    DPE_f06_receipt_lever,
    DPE_f07_hi_slip_sensor,
    DPE_f08_low_slip_sensor,
    DPE_f09_presenter,
    DPE_f10_presenter_commands,
    DPE_f11_ej_overflow_flag,
    DPE_f12_ej,
    DPE_f13_cutter,
    DPE_f14_drawer_status_as_presenter_paper_sensor,
    DPE_f15_drawer_sensor,
    DPE_f16_presenter_in_paper_sensor,
    DPE_f17_presenter_out_paper_sensor,
    DPE_f18_bill_acceptor,
    DPE_f19_tax_keyboard,
    DPE_f20_journal,
    DPE_f21_slip,
    DPE_f22_non_fiscal_doc_commands,
    DPE_f23_cashcore,
    DPE_f24_inn_leading_zeros,
    DPE_f25_rnm_leading_zeros,
    DPE_f26_line_printing_bytes_swapping,
    DPE_f27_wrong_tax_password_blocking,
    DPE_f28_alt_protocol,
    DPE_f29_string_printing_commands_wrap_strings_by_n,
    DPE_f30_string_printing_commands_wrap_strings_by_font,
    DPE_f31_fisc_commands_wrap_strings_by_n,
    DPE_f32_fisc_commands_wrap_strings_by_font,
    DPE_f33_senior_cashier,
    DPE_f34_slip_receipt_bit3,
    DPE_f35_block_graphic_loading,
    DPE_f36_error_description_command,
    DPE_f37_print_flags_for_print_ext_graphics_print_line,
    DPE_f38_skno,
    DPE_f39_mfp,
    DPE_f40_ej5,
    DPE_f41_print_scaled_graphics,
    DPE_f42_print_ext_graphics_512,
    DPE_f43_fs,
    DPE_f44_eod,
    DPE_f45_tag_autoprint_support,
    DPE_f46_qr_in_footer_support,
    DPE_f47_fs_1_1_support,
    DPE_f48_correction_new_support,
    DPE_f49_error_description_command_extended,
    DPE_f50_fd_answers_extended,
    DPE_f51_fd_authorization_req,
    DPE_f52_plain_protocolv1_transfer,
    DPE_f53_blocking_mode_available,
    DPE_reserved,
    DPE_Font1Width = 64,
    DPE_Font2Width,
    DPE_FirstDrawLine,
    DPE_InnDigitCount,
    DPE_RnmDigitCount,
    DPE_LongRnmDigitCount,
    DPE_LongSerialDigitCount,
    DPE_DefaultTaxPassword,
    DPE_DefaultAdminPassword,
    DPE_BluetoothTableNumber,
    DPE_TaxFieldNumber,
    DPE_MaxCmdLength,
    DPE_MaxDrawLineWidth,
    DPE_MaxDrawLineWidth512,
    DPE_MaxDrawLineCount512,
    DPE_FsTableNumber,
    DPE_OfdTableNmb,
    DPE_EmbeddedTableNumber,
    DPE_FFDVersionTableNumber,
    DPE_FFDVersionFieldNumber,
};
enum ESwapBytesMode {
    SBM_Swap = 0,
    SBM_NoSwap = 1,
    SBM_Prop = 2,
    SBM_Model = 3,
};
enum PrinterMode {
    PM_UnknownMode = 0x0,
    PM_DumpMode = 0x01,
    PM_SessionOpen = 0x02,
    PM_SessionOpenOver24h = 0x03,
    PM_SessionClosed = 0x04,
    PM_TaxmanPasswordError = 0x05,
    PM_DateConfirmWaiting = 0x06,
    PM_PointModificationAllowed = 0x07,
    PM_OpenedDocument = 0x08,
    PM_TechnologicalResetAllowed = 0x09,
    PM_TestRun = 0x0A,
    PM_FullFiscalReportInProgress = 0x0B,
    PM_CryptoJournalReportInProgress = 0x0C,
    PM_FiscalSlipMode = 0x0D,
    PM_SlipPrintingInProgress = 0x0E,
    PM_FiscalSlipIsReady = 0x0F,
    PM_OpenedDocumentBuy = 0x18,
    PM_OpenedSlipDocumentBuy = 0x1D,
    PM_LoadingAndPositioningSlip = 0x1E,
    PM_OpenedDocumentSaleReturn = 0x28,
    PM_OpenedSlipDocumentSaleReturn = 0x2D,
    PM_PositioningSlip = 0x2E,
    PM_OpenedDocumentBuyReturn = 0x38,
    PM_OpenedSlipDocumentBuyReturn = 0x3D,
    PM_PrintingSlip = 0x3E,
    PM_OpenedDocumentNonFiscal = 0x48,
    PM_SlipPrinted = 0x4C,
    PM_DocumentPrinted = 0x4E,
    PM_EjectingSlip = 0x5E,
    PM_WaitingSlipRemoval = 0x6E,
};
enum PrinterSubmode {
    PSM_PaperPresent = 0,
    PSM_PassivePaperAbsense = 1,
    PSM_ActivePaperAbsense = 2,
    PSM_AfterAvtivePaperAbsense = 3,
    PSM_ReportPrintingInProgress = 4,
    PSM_OperationPrintingInProgress = 5
};
enum DeviceFunctionEnumeration {
    DFE_SkipAllPrinting = 0,
    DFE_AutoReadDetailedErrorDescription = 1,
    DFE_DataPresentation = 2,
    DFE_PlainTransfer = 3,
    DFE_BlockingMode = 4,
};
enum DataPresentationFormat {
    DPF_ClassicText = 0,
    DPF_ClassicJson = 1,
};
enum TagTypeEnumeration : int {
    TT_Byte = 0, ///> Тип Byte
    TT_Uint16 = 1, ///> Тип Uint16
    TT_Uint32 = 2, ///> Тип UInt32
    TT_VLN = 3, ///> Тип VLN
    TT_FVLN = 4, ///> Тип FVLN
    TT_BitMask = 5, ///> Тип "битовое поле"
    TT_UnixTime = 6, ///> Тип "время"
    TT_String = 7, ///> Тип "строка".
};

/**
 * @brief Мера количества предмета расчета, свойство MeasureUnit (тег 2108)
 */
enum MeasurementUnitEnumeration : int {
    MU_Item
    = 0, ///< Применяется для предметов расчета, которые могут быть реализованы поштучно или единицами
    MU_Gram = 10, ///< Грамм
    MU_Kilogram = 11, ///< Килограмм
    MU_Ton = 12, ///< Тонна
    MU_Centimeter = 20, ///< Сантиметр
    MU_Decimeter = 21, ///< Дециметр
    MU_Meter = 22, ///< Метр
    MU_SquareCentimeter = 30, ///< Квадратный сантиметр
    MU_SquareDecimeter = 31, ///< Квадратный дециметр
    MU_SquareMeter = 32, ///< Квадратный метр
    MU_Milliliter = 40, ///< Миллилитр
    MU_Liter = 41, ///< Литр
    MU_CubicMeter = 42, ///< Кубический метр
    MU_KilowattHour = 50, ///< Киловатт час
    MU_Gigacalorie = 51, ///< Гигакалория
    MU_Day = 70, ///< Сутки (день)
    MU_Hour = 71, ///< Час
    MU_Minute = 72, ///< Минута
    MU_Second = 73, ///< Секунда
    MU_Kilobyte = 80, ///< Килобайт
    MU_Megabyte = 81, ///< Мегабайт
    MU_Gigabyte = 82, ///< Гигабайт
    MU_Terabyte = 83, ///< Терабайт
    MU_Other = 255, ///< Применяется при использовании иных единиц измерения
};
/**
 * C wrapper for classic_fr_drv_ng
 * 1. all methods takes c_classic_context_t pointer as first argument
 * 2. all array-like setters (std::string/std::vector<uint8_t>) taking (const char* value, size_t len),
 * because they may contain null bytes...
 * 3. if you want driver to calculate const char * (string) size by itself you must pass SIZE_MAX len.
 * 4. all array-like getters returns real output size, but copying to out_value up to size_t in_size bytes
 * 5. all int/bool/int64/double setters/getters work just like c++ class members except that
 * you must pass c_classic_context_t as first argument
 */
struct c_classic_context;
typedef struct c_classic_context c_classic_context_t;

/**
 * @brief c_classic_init
 * @param instance_prefix if NULL - default classic_interface used
 * @return new context or NULL if error
 */
C_CLASSIC_FR_DRV_NGX_API c_classic_context_t* c_classic_init(const char* instance_prefix);
/**
 * @brief c_classic_deinit destroy context and free resources
 * @param ctx to destroy
 */
C_CLASSIC_FR_DRV_NGX_API void c_classic_deinit(c_classic_context_t* ctx);

C_CLASSIC_FR_DRV_NGX_API int AddLD(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Beep(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Buy(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int BuyEx(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int CancelCheck(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int CashIncome(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int CashOutcome(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Charge(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int CheckSubTotal(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int CloseCheck(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ConfirmDate(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Connect(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ContinuePrint(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Correction(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int CutCheck(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int DampRequest(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int DeleteLD(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Disconnect(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Discount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int DozeOilCheck(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Draw(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int EKLZDepartmentReportInDatesRange(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int EKLZDepartmentReportInSessionsRange(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int EKLZJournalOnSessionNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int EKLZSessionReportInDatesRange(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int EKLZSessionReportInSessionsRange(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ExchangeBytes(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FeedDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Fiscalization(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FiscalReportForDatesRange(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FiscalReportForSessionRange(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetActiveLD(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int EnumLD(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetCashReg(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetCountLD(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetData(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetDeviceMetrics(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetECRStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetShortECRStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetExchangeParam(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetFieldStruct(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetFiscalizationParameters(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetFMRecordsSum(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetLastFMRecordDate(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetLiterSumCounter(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetOperationReg(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetParamLD(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetRangeDatesAndSessions(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetRKStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetTableStruct(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int InitFM(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int InitTable(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int InterruptDataStream(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int InterruptFullReport(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int InterruptTest(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int LaunchRK(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int LoadLineData(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int OilSale(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int OpenCheck(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int OpenDrawer(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int PrintBarCode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int PrintDepartmentReport(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int PrintDocumentTitle(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int PrintOperationReg(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int PrintReportWithCleaning(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int PrintReportWithoutCleaning(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int PrintString(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int PrintWideString(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ReadEKLZDocumentOnKPK(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ReadEKLZSessionTotal(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ReadLicense(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ReadTable(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int RepeatDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ResetAllTRK(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ResetRK(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ResetSettings(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ResetSummary(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ReturnBuy(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ReturnBuyEx(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ReturnSale(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ReturnSaleEx(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Sale(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int SaleEx(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int SetActiveLD(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int SetDate(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int SetDozeInMilliliters(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int SetDozeInMoney(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int SetExchangeParam(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int SetParamLD(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int SetPointPosition(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int SetRKParameters(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int SetSerialNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int SetTime(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ShowProperties(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int StopEKLZDocumentPrinting(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int StopRK(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Storno(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int StornoEx(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int StornoCharge(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int StornoDiscount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int SummOilCheck(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int SysAdminCancelCheck(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Test(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int WriteLicense(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int WriteTable(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int PrintStringWithFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_BarCode(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_BarCode(c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API bool Get_BatteryCondition(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API double Get_BatteryVoltage(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_BaudRate(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_BaudRate(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_Change(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_CheckResult(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CheckResult(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int Get_CheckType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CheckType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_ComNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ComNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_ContentsOfCashRegister(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_ContentsOfOperationRegister(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_CurrentDozeInMilliliters(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CurrentDozeInMilliliters(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_CurrentDozeInMoney(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CurrentDozeInMoney(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API bool Get_CutType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CutType(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_DataBlock(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int Get_DataBlockNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API time_t Get_Date(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Date(c_classic_context_t* ctx, time_t value);
C_CLASSIC_FR_DRV_NGX_API int Get_Department(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Department(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_DeviceCode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DeviceCode(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_DeviceCodeDescription(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API double Get_DiscountOnCheck(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DiscountOnCheck(c_classic_context_t* ctx, double value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_DocumentName(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_DocumentName(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API uint32_t Get_DocumentNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DocumentNumber(c_classic_context_t* ctx, uint32_t value);
C_CLASSIC_FR_DRV_NGX_API int Get_DozeInMilliliters(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DozeInMilliliters(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_DozeInMoney(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DozeInMoney(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int Get_DrawerNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DrawerNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_ECRAdvancedMode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_ECRAdvancedModeDescription(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int Get_ECRBuild(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_ECRFlags(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_ReceiptRibbonIsPresent(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_JournalRibbonIsPresent(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_SlipDocumentIsPresent(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_SlipDocumentIsMoving(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_PointPosition(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_PointPosition(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API bool Get_EKLZIsPresent(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_JournalRibbonOpticalSensor(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_ReceiptRibbonOpticalSensor(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_JournalRibbonLever(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_ReceiptRibbonLever(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_LidPositionSensor(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_IsDrawerOpen(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_IsPrinterRightSensorFailure(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_IsPrinterLeftSensorFailure(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_IsEKLZOverflow(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_QuantityPointPosition(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_SKNOStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SKNOStatus(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_ECRInput(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int Get_ECRMode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_ECRMode8Status(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_ECRModeDescription(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API size_t Get_ECROutput(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API time_t Get_ECRSoftDate(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_ECRSoftVersion(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int Get_EmergencyStopCode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_EmergencyStopCodeDescription(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API size_t Get_FieldName(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int Get_FieldNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_FieldNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_FieldSize(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_FieldType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_FirstLineNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_FirstLineNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API time_t Get_FirstSessionDate(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_FirstSessionDate(c_classic_context_t* ctx, time_t value);
C_CLASSIC_FR_DRV_NGX_API int Get_FirstSessionNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_FirstSessionNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_FMBuild(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_FMFlags(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_FM1IsPresent(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_FM2IsPresent(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_LicenseIsPresent(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_FMOverflow(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_IsBatteryLow(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_IsLastFMRecordCorrupted(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_IsFMSessionOpen(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_IsFM24HoursOver(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API time_t Get_FMSoftDate(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_FMSoftVersion(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int Get_FreeRecordInFM(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_FreeRegistration(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_INN(c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_INN(c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API bool Get_IsCheckClosed(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_IsCheckMadeOut(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_KPKNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_KPKNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_LastLineNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_LastLineNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API time_t Get_LastSessionDate(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_LastSessionDate(c_classic_context_t* ctx, time_t value);
C_CLASSIC_FR_DRV_NGX_API int Get_LastSessionNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_LastSessionNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_License(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_License(c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API size_t Get_LineData(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_LineData(c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int Get_LineNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_LineNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_LogicalNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_MAXValueOfField(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_MINValueOfField(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_Motor(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_NameCashReg(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API size_t Get_NameOperationReg(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API uint32_t Get_NewPasswordTI(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_NewPasswordTI(c_classic_context_t* ctx, uint32_t value);
C_CLASSIC_FR_DRV_NGX_API int Get_OpenDocumentNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_OperatorNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API uint32_t Get_Password(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Password(c_classic_context_t* ctx, uint32_t value);
C_CLASSIC_FR_DRV_NGX_API bool Get_Pistol(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_PortNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_PortNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_Price(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Price(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API double Get_Quantity(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Quantity(c_classic_context_t* ctx, double value);
C_CLASSIC_FR_DRV_NGX_API int Get_QuantityOfOperations(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_RegisterNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_RegisterNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_RegistrationNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_RegistrationNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API bool Get_ReportType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ReportType(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int Get_ResultCode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_ResultCodeDescription(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int Get_RKNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_RKNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_RNM(c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_RNM(c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API bool Get_RoughValve(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_RowNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_RowNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_RunningPeriod(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_RunningPeriod(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_SerialNumber(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_SerialNumber(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int Get_SessionNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SessionNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_SlowingInMilliliters(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SlowingInMilliliters(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API bool Get_SlowingValve(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_StatusRK(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_StatusRKDescription(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API size_t Get_StringForPrinting(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_StringForPrinting(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int Get_StringQuantity(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_StringQuantity(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_Summ1(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ1(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_Summ2(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ2(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_Summ3(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ3(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_Summ4(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ4(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_TableName(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int Get_TableNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TableNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax1(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax1(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax2(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax2(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax3(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax3(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax4(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax4(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API time_t Get_Time(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Time(c_classic_context_t* ctx, time_t value);
C_CLASSIC_FR_DRV_NGX_API int Get_Timeout(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Timeout(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_TimeStr(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_TimeStr(c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API size_t Get_TransferBytes(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_TransferBytes(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int Get_TRKNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TRKNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API bool Get_TypeOfLastEntryFM(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_TypeOfSumOfEntriesFM(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TypeOfSumOfEntriesFM(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int Get_UCodePage(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_UDescription(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int Get_UMajorProtocolVersion(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_UMajorType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_UMinorProtocolVersion(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_UMinorType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_UModel(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_UseJournalRibbon(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_UseJournalRibbon(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API bool Get_UseReceiptRibbon(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_UseReceiptRibbon(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API bool Get_UseSlipDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_UseSlipDocument(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int Get_ValueOfFieldInteger(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ValueOfFieldInteger(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_ValueOfFieldString(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_ValueOfFieldString(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int Get_FontType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_FontType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_LDBaudrate(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_LDBaudrate(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_LDComNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_LDComNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_LDCount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_LDIndex(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_LDIndex(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_LDName(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_LDName(c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int Get_LDNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_LDNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_WaitPrintingTime(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int EKLZActivizationResult(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int EKLZActivization(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int CloseEKLZArchive(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetEKLZSerialNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_EKLZNumber(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int EKLZInterrupt(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetEKLZCode1Report(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_LastKPKDocumentResult(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API time_t Get_LastKPKDate(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API time_t Get_LastKPKTime(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_LastKPKNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_EKLZFlags(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetEKLZCode2Report(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int TestEKLZArchiveIntegrity(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_TestNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TestNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_EKLZVersion(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API size_t Get_EKLZData(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int GetEKLZVersion(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int InitEKLZArchive(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetEKLZData(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetEKLZJournal(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetEKLZDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetEKLZDepartmentReportInDatesRange(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetEKLZDepartmentReportInSessionsRange(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetEKLZSessionReportInDatesRange(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetEKLZSessionReportInSessionsRange(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetEKLZSessionTotal(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetEKLZActivizationResult(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int SetEKLZResultCode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_EKLZResultCode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_EKLZResultCode(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_FMResultCode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API double Get_PowerSourceVoltage(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int OpenFiscalSlipDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int OpenStandardFiscalSlipDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int RegistrationOnSlipDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int StandardRegistrationOnSlipDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ChargeOnSlipDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int StandardChargeOnSlipDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int CloseCheckOnSlipDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int StandardCloseCheckOnSlipDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ConfigureSlipDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ConfigureStandardSlipDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FillSlipDocumentWithUnfiscalInfo(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ClearSlipDocumentBufferString(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ClearSlipDocumentBuffer(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int PrintSlipDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_CopyType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CopyType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_NumberOfCopies(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_NumberOfCopies(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_CopyOffset1(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CopyOffset1(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_CopyOffset2(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CopyOffset2(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_CopyOffset3(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CopyOffset3(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_CopyOffset4(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CopyOffset4(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_CopyOffset5(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CopyOffset5(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_ClicheFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ClicheFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_HeaderFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_HeaderFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_EKLZFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_EKLZFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_ClicheStringNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ClicheStringNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_HeaderStringNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_HeaderStringNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_EKLZStringNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_EKLZStringNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_FMStringNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_FMStringNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_ClicheOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ClicheOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_HeaderOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_HeaderOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_EKLZOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_EKLZOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_KPKOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_KPKOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_FMOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_FMOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_OperationBlockFirstString(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_OperationBlockFirstString(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_QuantityFormat(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_QuantityFormat(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_StringQuantityInOperation(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_StringQuantityInOperation(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_TextStringNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TextStringNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_QuantityStringNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_QuantityStringNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_SummStringNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SummStringNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_DepartmentStringNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DepartmentStringNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_TextFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TextFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_QuantityFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_QuantityFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_MultiplicationFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_MultiplicationFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_PriceFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_PriceFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_SummFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SummFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_DepartmentFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DepartmentFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_TextSymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TextSymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_QuantitySymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_QuantitySymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_PriceSymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_PriceSymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_SummSymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SummSymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_DepartmentSymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DepartmentSymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_TextOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TextOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_QuantityOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_QuantityOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_SummOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SummOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_DepartmentOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DepartmentOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int DiscountOnSlipDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int StandardDiscountOnSlipDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_IsClearUnfiscalInfo(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_IsClearUnfiscalInfo(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int Get_InfoType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_InfoType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_StringNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_StringNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int EjectSlipDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_EjectDirection(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_EjectDirection(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int LoadLineDataEx(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int DrawEx(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ConfigureGeneralSlipDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_OperationNameStringNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_OperationNameStringNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_OperationNameFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_OperationNameFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_OperationNameOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_OperationNameOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_TotalStringNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TotalStringNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Summ1StringNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ1StringNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Summ2StringNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ2StringNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Summ3StringNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ3StringNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Summ4StringNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ4StringNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_ChangeStringNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ChangeStringNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax1TurnOverStringNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax1TurnOverStringNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax2TurnOverStringNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax2TurnOverStringNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax3TurnOverStringNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax3TurnOverStringNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax4TurnOverStringNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax4TurnOverStringNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax1SumStringNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax1SumStringNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax2SumStringNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax2SumStringNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax3SumStringNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax3SumStringNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax4SumStringNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax4SumStringNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_SubTotalStringNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SubTotalStringNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_DiscountOnCheckStringNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DiscountOnCheckStringNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_TotalFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TotalFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_TotalSumFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TotalSumFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Summ1Font(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ1Font(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Summ1NameFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ1NameFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Summ2NameFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ2NameFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Summ3NameFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ3NameFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Summ4NameFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ4NameFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Summ2Font(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ2Font(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Summ3Font(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ3Font(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Summ4Font(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ4Font(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_ChangeFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ChangeFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_ChangeSumFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ChangeSumFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax1NameFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax1NameFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax2NameFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax2NameFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax3NameFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax3NameFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax4NameFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax4NameFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax1TurnOverFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax1TurnOverFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax2TurnOverFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax2TurnOverFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax3TurnOverFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax3TurnOverFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax4TurnOverFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax4TurnOverFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax1RateFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax1RateFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax2RateFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax2RateFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax3RateFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax3RateFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax4RateFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax4RateFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax1SumFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax1SumFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax2SumFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax2SumFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax3SumFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax3SumFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax4SumFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax4SumFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_SubTotalFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SubTotalFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_SubTotalSumFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SubTotalSumFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_DiscountOnCheckFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DiscountOnCheckFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_DiscountOnCheckSumFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DiscountOnCheckSumFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_TotalSymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TotalSymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Summ1SymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ1SymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Summ2SymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ2SymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Summ3SymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ3SymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Summ4SymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ4SymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_ChangeSymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ChangeSymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax1NameSymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax1NameSymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax1TurnOverSymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax1TurnOverSymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax1RateSymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax1RateSymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax1SumSymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax1SumSymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax2NameSymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax2NameSymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax2TurnOverSymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax2TurnOverSymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax2RateSymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax2RateSymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax2SumSymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax2SumSymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax3NameSymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax3NameSymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax3TurnOverSymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax3TurnOverSymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax3RateSymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax3RateSymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax3SumSymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax3SumSymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax4NameSymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax4NameSymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax4TurnOverSymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax4TurnOverSymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax4RateSymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax4RateSymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax4SumSymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax4SumSymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_SubTotalSymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SubTotalSymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_DiscountOnCheckSymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DiscountOnCheckSymbolNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_DiscountOnCheckSumSymbolNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DiscountOnCheckSumSymbolNumber(
    c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_TotalOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TotalOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Summ1Offset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ1Offset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_TotalSumOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TotalSumOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Summ1NameOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ1NameOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Summ2Offset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ2Offset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Summ2NameOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ2NameOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Summ3Offset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ3Offset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Summ3NameOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ3NameOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Summ4Offset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ4Offset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Summ4NameOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ4NameOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_ChangeOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ChangeOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_ChangeSumOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ChangeSumOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax1NameOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax1NameOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax1TurnOverOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax1TurnOverOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax1RateOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax1RateOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax1SumOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax1SumOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax2NameOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax2NameOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax2TurnOverOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax2TurnOverOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax2RateOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax2RateOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax2SumOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax2SumOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax3NameOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax3NameOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax3TurnOverOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax3TurnOverOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax3RateOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax3RateOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax3SumOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax3SumOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax4NameOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax4NameOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax4TurnOverOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax4TurnOverOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax4RateOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax4RateOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Tax4SumOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Tax4SumOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_SubTotalOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SubTotalOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_SubTotalSumOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SubTotalSumOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_SlipDocumentWidth(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SlipDocumentWidth(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_SlipDocumentLength(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SlipDocumentLength(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_PrintingAlignment(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_PrintingAlignment(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_SlipStringIntervals(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_SlipStringIntervals(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int Get_SlipEqualStringIntervals(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SlipEqualStringIntervals(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_KPKFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_KPKFont(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_DiscountOnCheckOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DiscountOnCheckOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_DiscountOnCheckSumOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DiscountOnCheckSumOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int WideLoadLineData(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int PrintTaxReport(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API uint32_t Get_FileVersionMS(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API uint32_t Get_FileVersionLS(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetLongSerialNumberAndLongRNM(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int SetLongSerialNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FiscalizationWithLongRNM(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Connect2(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_ECRModeStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetECRPrinterStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_PrinterStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_ServerVersion(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API size_t Get_LDComputerName(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_LDComputerName(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int Get_LDTimeout(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_LDTimeout(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_ComputerName(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_ComputerName(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int ServerConnect(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ServerDisconnect(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_ServerConnected(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int LockPort(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int UnlockPort(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_PortLocked(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int AdminUnlockPort(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int AdminUnlockPorts(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ServerCheckKey(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetFontMetrics(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_PrintWidth(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_CharWidth(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_CharHeight(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_FontCount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetFreeLDNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_LogOn(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_LogOn(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int ReadTable2(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int WriteTable2(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void SetFieldMinValue(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API void SetFieldMaxValue(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API bool Get_CPLog(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CPLog(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_CashControlHost(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_CashControlHost(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API size_t Get_CashControlPort(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_CashControlPort(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API bool Get_CashControlEnabled(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CashControlEnabled(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API bool Get_CashControlUseTCP(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CashControlUseTCP(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API uint32_t Get_CashControlPassword(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CashControlPassword(c_classic_context_t* ctx, uint32_t value);
C_CLASSIC_FR_DRV_NGX_API int CashControlOpen(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int CashControlClose(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API TConnectionType Get_ConnectionType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ConnectionType(c_classic_context_t* ctx, TConnectionType value);
C_CLASSIC_FR_DRV_NGX_API TConnectionType Get_LDConnectionType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_LDConnectionType(c_classic_context_t* ctx, TConnectionType value);
C_CLASSIC_FR_DRV_NGX_API int Get_TCPPort(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TCPPort(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_LDTCPPort(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_LDTCPPort(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_IPAddress(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_IPAddress(c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API size_t Get_LDIPAddress(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_LDIPAddress(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API bool Get_UseIPAddress(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_UseIPAddress(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API bool Get_LDUseIPAddress(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_LDUseIPAddress(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int SaveParams(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_CPLogFile(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_CPLogFile(c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API size_t Get_ComLogFile(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_ComLogFile(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API size_t Get_LineData2(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_LineData2(c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API uint32_t Get_SysAdminPassword(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SysAdminPassword(c_classic_context_t* ctx, uint32_t value);
C_CLASSIC_FR_DRV_NGX_API bool Get_RecoverError165(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_RecoverError165(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int Get_MaxRecoverCount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_MaxRecoverCount(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int GetEKLZCode1Status(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetEKLZCode2Status(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ReadWriteFM(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int PrintHeader(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int CloseCheckWithResult(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_OperationCode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_AccType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_AccType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_Address(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Address(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_WrittenByte(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_WrittenByte(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_ReadByte(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_TransferByte(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_TransferByte(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int Get_OperationType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_OperationType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int AboutBox(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_PresenterIn(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_PresenterOut(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int PresenterKeep(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int PresenterPush(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int OpenScreen(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int CloseScreen(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_ComLogOnlyErrors(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ComLogOnlyErrors(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int SetSCPassword(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API uint32_t Get_SCPassword(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SCPassword(c_classic_context_t* ctx, uint32_t value);
C_CLASSIC_FR_DRV_NGX_API uint32_t Get_NewSCPassword(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_NewSCPassword(c_classic_context_t* ctx, uint32_t value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_LastKPKDateStr(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API size_t Get_LastKPKTimeStr(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API bool MethodSupported(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_MethodName(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_MethodName(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API size_t Get_PropertyName(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_PropertyName(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API bool PropertySupported(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_LockTimeout(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_LockTimeout(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int LockPortTimeout(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_SlipStringInterval(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SlipStringInterval(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int GetIBMStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetShortIBMStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_IBMStatusByte1(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_IBMStatusByte2(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_IBMStatusByte3(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_IBMStatusByte4(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_IBMStatusByte5(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_IBMStatusByte6(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_IBMStatusByte7(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_IBMStatusByte8(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_IBMFlags(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_IBMDocumentNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_IBMLastSaleReceiptNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_IBMLastBuyReceiptNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_IBMLastReturnSaleReceiptNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_IBMLastReturnBuyReceiptNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_IBMSessionDay(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_IBMSessionMonth(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_IBMSessionYear(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_IBMSessionHour(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_IBMSessionMin(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_IBMSessionSec(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API time_t Get_IBMSessionDateTime(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_EscapeIP(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_EscapeIP(c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int Get_EscapePort(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_EscapePort(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_LDEscapeIP(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_LDEscapeIP(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int Get_LDEscapePort(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_LDEscapePort(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_EscapeTimeout(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_EscapeTimeout(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_LDEscapeTimeout(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_LDEscapeTimeout(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_CommandTimeout(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CommandTimeout(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API bool Get_UseCommandTimeout(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_UseCommandTimeout(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int Get_CommandCount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_CommandIndex(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CommandIndex(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int GetCommandParams(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int SetCommandParams(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int SaveCommandParams(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_CommandName(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int Get_CommandDefTimeout(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_CommandCode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int SetAllCommandsParams(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_TimeoutsUsing(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TimeoutsUsing(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int SetDefCommandsParams(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int OpenSession(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int WaitForPrinting(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_IntervalNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_IntervalNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_IntervalValue(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_IntervalValue(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int GetInterval(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int SetInterval(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_ParentWnd(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ParentWnd(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int ShowTablesDlg(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_MobilePayEnabled(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_MobilePayEnabled(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int Get_PayDepartment(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_PayDepartment(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_ParamsPageIndex(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ParamsPageIndex(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int ShowPayParams(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_SaleError(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SaleError(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int ReprintSlipDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_RealPayDepartment(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_RealPayDepartment(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int CardPayProperties(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_CardPayEnabled(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CardPayEnabled(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int Get_CardPayType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CardPayType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API bool Get_ccUseTextAsWareName(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_ccWareNameLineNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ccUseTextAsWareName(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API void Set_ccWareNameLineNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_ccHeaderLineCount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ccHeaderLineCount(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API bool Get_LogCommands(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_LogCommands(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API bool Get_LogMethods(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_LogMethods(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int PrintLine(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API TBarcodeAlignment Get_BarcodeAlignment(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_BarcodeAlignment(
    c_classic_context_t* ctx, TBarcodeAlignment value);
C_CLASSIC_FR_DRV_NGX_API int JournalClear(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int JournalGetRow(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_JournalEnabled(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_JournalEnabled(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_JournalRow(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int Get_JournalRowCount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_JournalRowNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_JournalRowNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_JournalText(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int JournalInit(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FindDevice(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int LoadParams(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FinishDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int PrintTrailer(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API TFinishDocumentMode Get_FinishDocumentMode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_FinishDocumentMode(
    c_classic_context_t* ctx, TFinishDocumentMode value);
C_CLASSIC_FR_DRV_NGX_API int Get_SerialNumberAsInteger(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_INNAsInteger(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API time_t Get_ECRDate(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ECRDate(c_classic_context_t* ctx, time_t value);
C_CLASSIC_FR_DRV_NGX_API time_t Get_ECRTime(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ECRTime(c_classic_context_t* ctx, time_t value);
C_CLASSIC_FR_DRV_NGX_API int Get_PrintBarcodeText(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_PrintBarcodeText(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int WaitForCheckClose(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetSummFactor(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetQuantityFactor(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ReadDeviceMetrics(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ReadEcrStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int SaveState(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int RestoreState(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_HasCashControlLicense(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_BufferingType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_BufferingType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_FileName(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_FileName(c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int LoadImage(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetCashAcceptorStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetCashAcceptorRegisters(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int CashAcceptorReport(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_FeedAfterCut(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_FeedAfterCut(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int Get_FeedLineCount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_FeedLineCount(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API uint32_t Get_DriverMajorVersion(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API uint32_t Get_DriverMinorVersion(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API uint32_t Get_DriverRelease(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API uint32_t Get_DriverBuild(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ClearResult(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int MasterPayClearBuffer(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int MasterPayAddTextBlock(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int MasterPayCreateMac(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_CashControlProtocols(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int LoadBlockData(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_BlockType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_BlockType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_BlockNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_BlockNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_BlockDataHex(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_BlockDataHex(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int Get_LogMaxFileSize(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_LogMaxFileSize(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_LogMaxFileCount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_LogMaxFileCount(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API TBinaryConversion Get_BinaryConversion(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_BinaryConversion(
    c_classic_context_t* ctx, TBinaryConversion value);
C_CLASSIC_FR_DRV_NGX_API TCodePage Get_CodePage(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CodePage(c_classic_context_t* ctx, TCodePage value);
C_CLASSIC_FR_DRV_NGX_API bool Get_PrintJournalBeforeZReport(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_PrintJournalBeforeZReport(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int GetEKLZCode3Report(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_TransmitStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_TransmitQueueSize(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_TransmitSessionNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_TransmitDocumentNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ReadModemParameter(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int WriteModemParameter(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_ParameterNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ParameterNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_ParameterValue(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_ParameterValue(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API bool Get_TranslationEnabled(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TranslationEnabled(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int Get_ModelIndex(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ModelIndex(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_ModelParamIndex(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ModelParamIndex(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_ModelParamCount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetPortNames(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_ReceiptOutputType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int OutputReceipt(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ReceiptOutputType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Sale2(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int PrintCliche(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int PrintBarcodeLine(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int PrintBarcodeGraph(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_BarcodeType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_BarcodeType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_BarcodeTypes(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API size_t Get_BarcodeAlignments(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int Get_BarWidth(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_BarWidth(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API bool Get_CapGetShortECRStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_WaitForPrintingDelay(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_WaitForPrintingDelay(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int ResetECR(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int PrintZReportFromBuffer(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int PrintZReportInBuffer(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_LineSwapBytes(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_LineSwapBytes(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int Get_LogFileMaxSize(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_LogFileMaxSize(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int ClearPrintBuffer(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ReadPrintBufferLine(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ReadPrintBufferLineNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_PrintBufferFormat(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_PrintBufferFormat(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_PrintBufferLineNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_NakCount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_NakCount(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_MaxAnswerReadCount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_MaxCommandSendCount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_MaxENQSendCount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_MaxAnswerReadCount(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API void Set_MaxCommandSendCount(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API void Set_MaxENQSendCount(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_LineDataHex(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_LineDataHex(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int Get_CommandRetryCount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CommandRetryCount(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API bool Get_CenterImage(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CenterImage(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API bool Get_ShowProgress(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ShowProgress(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int OpenNonfiscalDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int CloseNonFiscalDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_AttributeNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_AttributeValue(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int PrintAttribute(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_AttributeNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API void Set_AttributeValue(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int Get_ModelID(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_ModelParamValue(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ReadModelParamValue(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ModelID(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_ModelParamNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ModelParamNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int LoadCashControlParams(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_Connected(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Connected(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API uint32_t Get_EnteredTaxPassword(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_BanknoteCount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_BanknoteType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_CashAcceptorPollingMode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_Poll1(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_Poll2(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_BanknoteType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int ReadBanknoteCount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API uint32_t Get_LDSysAdminPassword(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_LDSysAdminPassword(c_classic_context_t* ctx, uint32_t value);
C_CLASSIC_FR_DRV_NGX_API int PrintOperationalTaxReport(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_CapOpenCheck(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_PollDescription(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int Get_ConnectionTimeout(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ConnectionTimeout(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int WaitConnection(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_ModelParamDescription(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int ReadModelParamDescription(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_DriverVersion(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int Get_HRIPosition(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int PrintBarcodeUsingPrinter(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_HRIPosition(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_KPKStr(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int CloseCheckWithKPK(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ReadEKLZActivizationParams(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetShortReportInDatesRange(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetShortReportInSessionRange(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ReadLastReceipt(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ReadLastReceiptLine(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ReadLastReceiptMac(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_TextBlock(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int Get_TextBlockNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TextBlock(c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API void Set_TextBlockNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int BeginDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int EndDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_PosControlReceiptSeparator(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_PosControlReceiptSeparator(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int Get_BarcodeDataLength(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_BarcodeParameter1(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_BarcodeParameter2(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_BarcodeParameter3(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_BarcodeParameter4(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_BarcodeParameter5(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Print2DBarcode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_BarcodeDataLength(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API void Set_BarcodeParameter1(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API void Set_BarcodeParameter2(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API void Set_BarcodeParameter3(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API void Set_BarcodeParameter4(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API void Set_BarcodeParameter5(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_BarcodeStartBlockNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_BarcodeStartBlockNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int LoadAndPrint2DBarcode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_ExciseCode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ExciseCode(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int ExcisableOperation(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ReadReportBufferLine(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_SaveSettingsType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SaveSettingsType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int ReadParams(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_ModelNames(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int Get_ModelsCount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_FMFlagsEx(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_FMMode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_IsASPDMode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_IsCorruptedFiscalizationInfo(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_IsCorruptedFMRecords(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_CarryStrings(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_DelayedPrint(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CarryStrings(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API void Set_DelayedPrint(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int GetCashRegEx(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_RegBuyRec(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_RegBuyReturnRec(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_RegBuyReturnSession(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_RegBuySession(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_RegSaleRec(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_RegSaleReturnRec(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_RegSaleReturnSession(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_RegSaleSession(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetWareBaseCashRegs(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_WareCode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_WareCode(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int PrintCashierReport(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int PrintHourlyReport(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int PrintWareReport(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int UpdateWare(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int CheckFM(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int RemoveWare(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_RecordCount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_CheckingType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CheckingType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_ErrorCode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ErrorCode(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int ReadErrorDescription(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ReadLastErrorDescription(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ReadWare(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_UseWareCode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_UseWareCode(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API bool Get_RequestErrorDescription(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_RequestErrorDescription(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_ErrorDescription(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API bool Get_AdjustRITimeout(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_AdjustRITimeout(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_UCodePageText(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API bool Get_ReconnectPort(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ReconnectPort(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API bool Get_DoNotSendENQ(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DoNotSendENQ(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int Get_SwapBytesMode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SwapBytesMode(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int ReadModelParam(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int InitEEPROM(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_CheckEJConnection(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_CheckFMConnection(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CheckEJConnection(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API void Set_CheckFMConnection(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int CheckConnection(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_BarcodeHex(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_BarcodeHex(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int ChangeProtocol(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_ProtocolType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ProtocolType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_LDProtocolType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_LDProtocolType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int GetECRParams(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ShowImportDlg(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_LastPrintResult(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_UseSlipCheck(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_UseSlipCheck(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int Get_TypeOfLastEntryFMEx(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int JournalOperation(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_AutoSensorValues(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_AutoSensorValues(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API bool Get_AutoStartSearch(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_SearchTimeout(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_AutoStartSearch(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API void Set_SearchTimeout(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_TCPConnectionTimeout(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TCPConnectionTimeout(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int MFPActivization(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int MFPCloseArchive(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int MFPGetPermitActivizationCode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int MFPGetCustomerCode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int MFPPrepareActivization(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int MFPSetCustomerCode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int MFPSetPermitActivizationCode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int MFPGetPrepareActivizationResult(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int CloseCheckEx(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_Summ5(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ5(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_Summ6(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ6(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_Summ7(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ7(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_Summ8(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ8(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_Summ9(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ9(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_Summ10(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ10(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_Summ11(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ11(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_Summ12(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ12(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_Summ13(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ13(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_Summ14(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ14(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_Summ15(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ15(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_Summ16(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ16(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_Summ17(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ17(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_Summ18(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ18(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_Summ19(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ19(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_Summ20(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ20(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int Get_CustomerCode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CustomerCode(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_PermitActivizationCode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_PermitActivizationCode(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_NameCashRegEx(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int Get_ActivizationStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ActivizationStatus(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_MFPStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_MFPStatus(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_KPKValue(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_KPKValue(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_ActivizationControlByte(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ActivizationControlByte(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_PrepareActivizationRemainCount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_PrepareActivizationRemainCount(
    c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_AnswerCode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_AnswerCode(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int GetMFPCode3Status(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_MFPNumber(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_MFPNumber(c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int Get_RequestType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_RequestType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_ReadTimeout(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ReadTimeout(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int ClearReportBuffer(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_IsBlockedByWrongTaxPassword(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_LastFMRecordType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ShowAdditionalParams(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_CloudCashdeskEnabled(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_ECRID(c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_CloudCashdeskEnabled(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API void Set_ECRID(c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int GetCloudCashdeskParams(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_KSAInfo(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_KSAInfo(c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int Get_HorizScale(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_HorizScale(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_VertScale(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_VertScale(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int DrawScale(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_BarcodeFirstLine(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_BarcodeFirstLine(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_SKNOError(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SKNOError(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_SKNOIdentifier(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_SKNOIdentifier(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int LoadGraphics512(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int PrintGraphics512(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_GraphBufferType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_GraphBufferType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_LineLength(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_LineLength(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_FNCurrentDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_FNCurrentDocument(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_FNDocumentData(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_FNDocumentData(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_FNLifeState(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_FNLifeState(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_FNSessionState(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_FNSessionState(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_FNSoftVersion(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_FNSoftVersion(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int Get_FNSoftType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_FNWarningFlags(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_FNWarningFlags(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_SyncTimeout(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SyncTimeout(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int FNGetExpirationTime(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNGetSerial(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNGetStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNGetVersion(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNBeginFiscalization(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNFiscalization(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API uint32_t Get_FiscalSign(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_FiscalSign(c_classic_context_t* ctx, uint32_t value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_FiscalSignAsString(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API size_t Get_KKTRegistrationNumber(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_KKTRegistrationNumber(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int Get_TaxType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TaxType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_WorkMode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_WorkMode(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int FNCancelDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNResetState(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNFindDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_DocumentType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DocumentType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API bool Get_OFDTicketReceived(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_OFDTicketReceived(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_DocumentData(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_DocumentData(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int FNOpenSession(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNSendTLV(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_TLVData(
    c_classic_context_t* ctx, uint8_t* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_TLVData(
    c_classic_context_t* ctx, const uint8_t* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int FNDiscountOperation(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNStorno(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_DataBlockSize(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DataBlockSize(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_DataLength(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DataLength(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int OFDExchange(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_OFDPort(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_OFDPort(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_OFDServer(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_OFDServer(c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int Get_OFDPollPeriod(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_OFDPollPeriod(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API bool Get_OFDEnabled(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_OFDEnabled(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int FNBeginCalculationStateReport(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNBeginCloseFiscalMode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNBeginCloseSession(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNBeginCorrectionReceipt(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNBeginOpenSession(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNBeginRegistrationReport(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNBuildCalculationStateReport(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNBuildCorrectionReceipt(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNBuildRegistrationReport(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNCloseFiscalMode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNCloseSession(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNGetCurrentSessionParams(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNGetInfoExchangeStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNGetOFDTicketByDocNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNGetUnconfirmedDocCount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNReadFiscalDocumentTLV(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNRequestFiscalDocumentTLV(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNBuildReregistrationReport(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNGetFiscalizationResult(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_DocumentCount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DocumentCount(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_ReceiptNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ReceiptNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_InfoExchangeStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_InfoExchangeStatus(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_MessageState(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_MessageState(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_MessageCount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_MessageCount(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_ReportTypeInt(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ReportTypeInt(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int FNDiscountTaxOperation(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNCloseCheckEx(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_ChargeValue(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_DiscountValue(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_TaxValue(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TaxValue(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API void Set_ChargeValue(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API void Set_DiscountValue(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int Get_RegistrationReasonCode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_RegistrationReasonCode(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_DiscountName(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_DiscountName(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int FNSendCustomerEmail(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_CustomerEmail(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_CustomerEmail(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int Annulment(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API time_t Get_Date2(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Date2(c_classic_context_t* ctx, time_t value);
C_CLASSIC_FR_DRV_NGX_API time_t Get_Time2(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Time2(c_classic_context_t* ctx, time_t value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_FiscalSignOFD(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_FiscalSignOFD(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API bool Get_AutoOpenSession(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_AutoOpenSession(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int FNDiscountChargeRN(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ExportTables(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ImportTables(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNSendTag(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_TagNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TagNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_TagType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TagType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API uint64_t Get_TagValueInt(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TagValueInt(c_classic_context_t* ctx, uint64_t value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_TagValueStr(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_TagValueStr(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API double Get_TagValueFVLN(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TagValueFVLN(c_classic_context_t* ctx, double value);
C_CLASSIC_FR_DRV_NGX_API time_t Get_TagValueDateTime(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TagValueDateTime(c_classic_context_t* ctx, time_t value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_TagValueBin(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_TagValueBin(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int Get_TagValueLength(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TagValueLength(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int ReadSerialNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNPrintOperatorConfirm(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNGetFiscalizationResultByNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int AnnulmentRB(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNGetTagDescription(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_TagDescription(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_TagDescription(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int FNPrintDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNGetDocumentAsString(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_ShowTagNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ShowTagNumber(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int Ping(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_URL(c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_URL(c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int Get_PingTime(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_PingTime(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_PingResult(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_PingResult(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API bool Get_ICSEnabled(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_ICSPollPeriod(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ICSEnabled(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API void Set_ICSPollPeriod(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int FNOperation(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNSendTLVOperation(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_RoundingSumm(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_RoundingSumm(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_TaxValue1(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TaxValue1(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_TaxValue2(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TaxValue2(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_TaxValue3(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TaxValue3(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_TaxValue4(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TaxValue4(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_TaxValue5(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TaxValue5(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_TaxValue6(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TaxValue6(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_TaxValue7(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TaxValue7(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_TaxValue8(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TaxValue8(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_TaxValue9(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TaxValue9(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_TaxValue10(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TaxValue10(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API bool Get_Summ1Enabled(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Summ1Enabled(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API bool Get_TaxValue1Enabled(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_TaxValue2Enabled(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_TaxValue3Enabled(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_TaxValue4Enabled(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_TaxValue5Enabled(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_TaxValue6Enabled(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_TaxValue7Enabled(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_TaxValue8Enabled(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_TaxValue9Enabled(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_TaxValue10Enabled(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_AddTaxesEnabled(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_TaxValueEnabled(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TaxValueEnabled(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API void Set_TaxValue1Enabled(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API void Set_TaxValue2Enabled(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API void Set_TaxValue3Enabled(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API void Set_TaxValue4Enabled(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API void Set_TaxValue5Enabled(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API void Set_TaxValue6Enabled(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API void Set_TaxValue7Enabled(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API void Set_TaxValue8Enabled(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API void Set_TaxValue9Enabled(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API void Set_TaxValue10Enabled(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API void Set_AddTaxesEnabled(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int Get_PaymentTypeSign(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_PaymentTypeSign(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_PaymentItemSign(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_PaymentItemSign(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int FNBuildCorrectionReceipt2(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_CalculationSign(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CalculationSign(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_CorrectionType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CorrectionType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_OFDReadTimeout(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_OFDReadTimeout(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int FNGetNonClearableSumm(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_AutoEoD(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_AutoEoD(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int ResetSerialNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int DBFindDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_DBFilePath(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_DBFilePath(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int DBPrintDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_KKTLicense(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_LicenseNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_PUKCode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ReadKKTLicenses(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_KKTLicense(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API void Set_LicenseNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API void Set_PUKCode(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API bool Get_OFDExchangeSuspended(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_OFDExchangeSuspended(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int CloseCheckBel(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_AutoOFDExchange(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_AutoOFDExchange(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int GetKKTLicenseByNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int WriteKKTLicense(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNSendSenderEmail(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_EmailAddress(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_EmailAddress(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_Discount1(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_Discount2(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_Discount3(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_Discount4(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_UseTaxDiscountBel(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Discount1(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API void Set_Discount2(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API void Set_Discount3(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API void Set_Discount4(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API void Set_UseTaxDiscountBel(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_Summ1AsString(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API size_t Get_Summ2AsString(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API size_t Get_Summ3AsString(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API size_t Get_Summ4AsString(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int DBGetNextDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int DBPrintNextDocument(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int DBQueryDocumentsInSession(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_DBDocType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DBDocType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_OPBarcodeInputType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_OPIdPayment(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int Get_OPRequisiteNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_OPRequisiteValue(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int Get_OPSystem(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_OPTransactionStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_OPTransactionType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int OnlinePay(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int OPGetLastRequisite(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int OPGetLastStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_OPBarcodeInputType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API void Set_OPIdPayment(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API void Set_OPRequisiteNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API void Set_OPRequisiteValue(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API void Set_OPSystem(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API void Set_OPTransactionStatus(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API void Set_OPTransactionType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_Token(c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int GenerateMonoToken(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Token(c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int RebootKKT(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNAddTag(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNBeginSTLVTag(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNSendSTLVTag(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNSendSTLVTagOperation(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNSendTagOperation(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_TagID(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_TagID(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API void Set_ConnectionURI(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API size_t Get_ConnectionURI(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int Get_SymbolCode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SymbolCode(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_SymbolWidth(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SymbolWidth(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_SymbolHeight(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SymbolHeight(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_FileType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_FileType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_BlockData(
    c_classic_context_t* ctx, uint8_t* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_BlockData(
    c_classic_context_t* ctx, const uint8_t* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int Get_DelayOnDisconnect(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DelayOnDisconnect(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API bool Get_WrapStrings(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_WrapStrings(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API void Set_GTIN(c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API size_t Get_GTIN(c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_MarkingType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_MarkingType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNSendItemCodeData(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNCheckItemBarcode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNRequestRegistrationTLV(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ReadLoaderVersion(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_LoaderVersion(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int Get_RequestDocumentType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_RequestDocumentType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int FNOpenCheckCorrection(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_WorkModeEx(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_WorkModeEx(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_INNOFD(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_INNOFD(c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int Get_RegistrationReasonCodeEx(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_RegistrationReasonCodeEx(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int FNCountersSync(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNGetFreeMemoryResource(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_SkipPrint(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_SkipPrint(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int ReadCashDrawerSum(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ReadFeatureLicenses(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int WriteFeatureLicenses(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_DigitalSign(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_DigitalSign(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int Get_DeviceFunctionNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DeviceFunctionNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_ValueOfFunctionInteger(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ValueOfFunctionInteger(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_ValueOfFunctionString(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_ValueOfFunctionString(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int SetDeviceFunction(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetDeviceFunction(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNSendItemBarcode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API bool Get_EnableCashcoreMarkCompatibility(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_EnableCashcoreMarkCompatibility(
    c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API void Set_MarkingTypeEx(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_MarkingTypeEx(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_MessageNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_MessageNumber(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int FNGetKMServerExchangeStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNGetMarkingCodeWorkStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNBeginReadNotifications(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNReadNotificationBlock(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNConfirmNotificationRead(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int GetTagAsTLV(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_CheckItemLocalError(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CheckItemLocalError(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_MeasureUnit(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_MeasureUnit(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API bool Get_DivisionalQuantity(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DivisionalQuantity(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API uint64_t Get_Numerator(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Numerator(c_classic_context_t* ctx, uint64_t value);
C_CLASSIC_FR_DRV_NGX_API uint64_t Get_Denominator(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_Denominator(c_classic_context_t* ctx, uint64_t value);
C_CLASSIC_FR_DRV_NGX_API int Get_FreeMemorySize(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_FreeMemorySize(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_MCCheckStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_MCCheckStatus(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_MCNotificationStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_MCNotificationStatus(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_MCCommandFlags(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_MCCommandFlags(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_MCCheckResultSavedCount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_MCCheckResultSavedCount(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_MCRealizationCount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_MCRealizationCount(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_MCStorageSize(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_MCStorageSize(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API uint64_t Get_CheckSum(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CheckSum(c_classic_context_t* ctx, uint64_t value);
C_CLASSIC_FR_DRV_NGX_API int Get_NotificationCount(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_NotificationCount(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_NotificationNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_NotificationNumber(c_classic_context_t* ctx, int64_t value);
C_CLASSIC_FR_DRV_NGX_API int Get_NotificationSize(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_NotificationSize(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_DataOffset(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DataOffset(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_MarkingType2(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_MarkingType2(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API size_t Get_RandomSequence(
    c_classic_context_t* ctx, uint8_t* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_RandomSequence(
    c_classic_context_t* ctx, const uint8_t* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API size_t Get_RandomSequenceHex(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_RandomSequenceHex(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int ReadRandomSequence(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Authorization(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_AuthData(
    c_classic_context_t* ctx, uint8_t* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_AuthData(
    c_classic_context_t* ctx, const uint8_t* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int FNAcceptMarkingCode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNDeclineMarkingCode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNBindMarkingItem(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int Get_ItemStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_ItemStatus(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_CheckItemMode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CheckItemMode(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_CheckItemLocalResult(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CheckItemLocalResult(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_KMServerErrorCode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_KMServerErrorCode(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_KMServerCheckingStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_KMServerCheckingStatus(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_LastDocumentNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_LastDocumentNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_FirstDocumentNumber(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_FirstDocumentNumber(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int Get_FNArchiveType(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_FNArchiveType(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API bool Get_MarkingOnly(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_MarkingOnly(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int FNBeginReadArchive(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNReadArchiveItem(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNSaveArchive(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNMarkingClearBuffer(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNSendUserAttribute(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API size_t Get_UserAttributeName(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API size_t Get_UserAttributeValue(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_UserAttributeValue(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API void Set_UserAttributeName(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int64_t Get_WaitForPrintingTimeout(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_WaitForPrintingTimeout(c_classic_context_t* ctx, int64_t value);

C_CLASSIC_FR_DRV_NGX_API size_t Get_DeclarativeInput(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_DeclarativeInput(
    c_classic_context_t* ctx, const char* value, size_t len);

C_CLASSIC_FR_DRV_NGX_API size_t Get_DeclarativeOutput(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_DeclarativeOutput(
    c_classic_context_t* ctx, const char* value, size_t len);

C_CLASSIC_FR_DRV_NGX_API size_t Get_DeclarativeEndpointPath(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_DeclarativeEndpointPath(
    c_classic_context_t* ctx, const char* value, size_t len);
C_CLASSIC_FR_DRV_NGX_API int RenderDeclarativeDocument(c_classic_context_t* ctx);

C_CLASSIC_FR_DRV_NGX_API size_t Get_DataBlockHex(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int LoadFont(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ReadFontHash(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int ResetFont(c_classic_context_t* ctx);

C_CLASSIC_FR_DRV_NGX_API size_t Get_FontHashHex(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API int LoadFontSymbol(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int DecodeTLVData(c_classic_context_t* ctx);

C_CLASSIC_FR_DRV_NGX_API bool Get_MCOSUSign(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_MCOSUSign(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int FNGetImplementation(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNGetOSUSupportStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int FNGetDocumentSize(c_classic_context_t* ctx);

C_CLASSIC_FR_DRV_NGX_API int Get_DocumentSize(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_DocumentSize(c_classic_context_t* ctx, int value);

C_CLASSIC_FR_DRV_NGX_API size_t Get_FNImplementation(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_FNImplementation(
    c_classic_context_t* ctx, const char* value, size_t len);

C_CLASSIC_FR_DRV_NGX_API int Get_FNOSUSupportStatus(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_FNOSUSupportStatus(c_classic_context_t* ctx, int value);
C_CLASSIC_FR_DRV_NGX_API int FNReadFiscalBarcode(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API int PrintStringWithWrap(c_classic_context_t* ctx);

C_CLASSIC_FR_DRV_NGX_API bool Get_CrptCheck(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_CrptCheck(c_classic_context_t* ctx, bool value);
C_CLASSIC_FR_DRV_NGX_API int FNCheckItemBarcodeCrpt(c_classic_context_t* ctx);

C_CLASSIC_FR_DRV_NGX_API size_t Get_InputStrJson(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_InputStrJson(
    c_classic_context_t* ctx, const char* value, size_t len);

C_CLASSIC_FR_DRV_NGX_API size_t Get_OutputStrJson(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_OutputStrJson(
    c_classic_context_t* ctx, const char* value, size_t len);

C_CLASSIC_FR_DRV_NGX_API size_t Get_CrptToken(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_CrptToken(c_classic_context_t* ctx, const char* value, size_t len);

C_CLASSIC_FR_DRV_NGX_API size_t Get_CrptCdnListUrl(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_CrptCdnListUrl(
    c_classic_context_t* ctx, const char* value, size_t len);

C_CLASSIC_FR_DRV_NGX_API size_t Get_CrptExchangeCaCertPath(
    c_classic_context_t* ctx, char* out_value, size_t in_size);
C_CLASSIC_FR_DRV_NGX_API void Set_CrptExchangeCaCertPath(
    c_classic_context_t* ctx, const char* value, size_t len);

C_CLASSIC_FR_DRV_NGX_API uint32_t Get_FN5YearResource(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_FN5YearResource(c_classic_context_t* ctx, uint32_t value);

C_CLASSIC_FR_DRV_NGX_API uint32_t Get_FN30DayResource(c_classic_context_t* ctx);
C_CLASSIC_FR_DRV_NGX_API void Set_FN30DayResource(c_classic_context_t* ctx, uint32_t value);

typedef void (*property_changed_callback)(c_classic_context_t* ctx, const char*, size_t len);
typedef void (*log_callback)(const char*, size_t len);

C_CLASSIC_FR_DRV_NGX_API void setPropertyChangedCallback(
    c_classic_context_t* ctx, property_changed_callback callback);
C_CLASSIC_FR_DRV_NGX_API void setLogCallback(log_callback callback);

#ifdef __cplusplus
}
#endif
}
#endif // C_CLASSIC_API_H