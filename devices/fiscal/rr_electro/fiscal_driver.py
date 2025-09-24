import fr_drv_ngx


class BaseFiscal:
    """Базовый класс фискального регистратора."""
    def __init__(self, port="/dev/ttyNXP", password=30):
        self.port = port
        self.password = password

        # Создание экземпляра драйвера
        self.driver = fr_drv_ngx.classic_interface()
        self.driver.ConnectionType = self.driver.TConnectionType_Local
        self.driver.ConnectionURI = f"serial://{self.port}?timeout=15000&baudrate=115200&protocol=v1"
        self.driver.Password = self.password

    def connect(self):
        """Подключение к ККТ."""
        return self.driver.Connect()

    def disconnect(self):
        """Отключение от ККТ."""
        return self.driver.Disconnect()


class FiscalStorage(BaseFiscal):
    """Класс для управления фискальным накопителем."""
    def open_shift(self):
        """Открытие смены."""
        return self.driver.FNOpenSession()

    def close_shift(self):
        """Закрытие смены."""
        return self.driver.FNCloseSession()

    def get_fiscal_document(self, document_number: int):
        """Получение фискального документа."""
        self.driver.DocumentNumber = document_number
        return self.driver.FNGetDocumentAsString()

    def read_current_fiscal_document(self):
        """Чтение полученного документа в методе 'get_fiscal_document'."""
        return self.driver.StringForPrinting

    def get_fn_status(self):
        """Запрос статуса ФН."""
        return self.driver.FNGetStatus()

    def read_fn_status(self):
        """Чтение статуса ФН."""
        return {
            'FNLifeState': self.driver.FNLifeState,
            'FNCurrentDocument': self.driver.FNCurrentDocument,
            'FNDocumentData': self.driver.FNDocumentData,
            'FNSessionState': self.driver.FNSessionState,
            'FNWarningFlags': self.driver.FNWarningFlags,
            'Date': str(self.driver.Date),
            'Time': str(self.driver.Time),
            'SerialNumber': self.driver.SerialNumber,
            'DocumentNumber': self.driver.DocumentNumber,
        }

    def open_check(self, check_type: int):
        """
        Открытие чека.

        Check_type:
            0: 'продажа/приход'
            1: 'покупка/расход'
            2: 'возврат продажи/возврат прихода'
            3: 'возврат покупки/возврат расхода'
        """
        self.driver.CheckType = check_type
        return self.driver.OpenCheck()

    def close_check(
        self,
        payment_method: int,
        summ_total: int,
        tax_value1: int,
        tax_value2: int,
        advance_payment: int,
    ):
        """
        Закрытие чека.
        """
        # добавление авансового платежа
        if advance_payment:
            summ_total -= advance_payment
        if payment_method == 0:
            # наличные
            self.driver.Summ1 = summ_total
            self.driver.Summ2 = 0
        elif payment_method == 1:
            # электронные
            self.driver.Summ2 = summ_total
            self.driver.Summ1 = 0

        self.driver.Summ3 = 0
        self.driver.Summ4 = 0
        self.driver.Summ5 = 0
        self.driver.Summ6 = 0
        self.driver.Summ7 = 0
        self.driver.Summ8 = 0
        self.driver.Summ9 = 0
        self.driver.Summ10 = 0
        self.driver.Summ11 = 0
        self.driver.Summ12 = 0
        self.driver.Summ13 = 0
        self.driver.Summ14 = advance_payment
        self.driver.Summ15 = 0
        self.driver.Summ16 = 0

        self.driver.TaxValue1 = tax_value1
        self.driver.TaxValue2 = tax_value2
        self.driver.TaxValue3 = 0
        self.driver.TaxValue4 = 0
        self.driver.TaxValue5 = 0
        self.driver.TaxValue6 = 0

        self.driver.TaxType = 1

        self.driver.StringForPrinting = "Спасибо за покупку!"

        return self.driver.FNCloseCheckEx()

    def cancel_check(self):
        """Отмена открытого чека."""
        return self.driver.CancelCheck()

    def set_fair_mark(self, fair_mark: str):
        """Установка честного знака в чек."""
        # barcode = fair_mark.replace('\x1d', chr(29))
        # f'0104650167230503215ph.SS9k5qW*D' + chr(29) + '91EE10' + chr(29) + '92lX2OSKoVye4XdAPnOKn9AbQpDSTr0r7O2vrGeQP2Rzw='
        self.driver.BarCode = fair_mark
        return self.driver.FNSendItemBarcode()

    def set_tags_for_mark(self, req_id: str, req_timestamp: str):
        self.driver.TagNumber = 1262
        self.driver.TagType = 7
        self.driver.TagValueStr = '030'
        self.driver.FNSendTagOperation()

        self.driver.TagNumber = 1263
        self.driver.TagType = 7
        self.driver.TagValueStr = '21.11.2023'
        self.driver.FNSendTagOperation()

        self.driver.TagNumber = 1264
        self.driver.TagType = 7
        self.driver.TagValueStr = '1944'
        self.driver.FNSendTagOperation()

        self.driver.TagNumber = 1265
        self.driver.TagType = 7
        self.driver.TagValueStr = f'UUID={req_id}&Time={req_timestamp}'
        self.driver.FNSendTagOperation()


    def register_item(
        self,
        quantity: float,
        price: int,
        tax: int,
        name: str,
        check_type: int,
        tax_value: int,
        fair_mark: str | None = None,
    ):
        """
        Регистрация позиции чека.

        Сheck_type:
             1: 'продажа/приход'
             3: 'покупка/расход'
             2: 'возврат продажи/возврат прихода'
             4: 'возврат покупки/возврат расхода'
        VAT_RATES:
            0: 'БЕЗ НДС'
            1: 'НДС 20%'
            2: 'НДС 10%'
            3: 'НДС 0%'
        PaymentItemSign:
            1: 'товар'
            31: 'Акцизный маркированный товар'
            33: 'Маркированный товар'
        """
        self.driver.CheckType = check_type
        self.driver.Quantity = quantity
        self.driver.Price = price
        self.driver.Summ1Enabled = False
        self.driver.Tax1 = tax
        self.driver.TaxValueEnabled = True
        self.driver.TaxValue = tax_value
        self.driver.PaymentTypeSign = 4 # полный рассчет
        if fair_mark:
            self.driver.PaymentItemSign = 33
        else:
            self.driver.PaymentItemSign = 1
        self.driver.StringForPrinting = name

        return self.driver.FNOperation()

    def repeat_document(self):
        """Печать последнего закрытого документа продажи, покупки, возврата продажи и возврата покупки."""
        return self.driver.RepeatDocument()

    def print_x_report(self):
        """Формирование и печать X-отчета."""
        return self.driver.PrintReportWithoutCleaning()

    def set_tag(self, tag_number, tag_value):
        self.driver.TagNumber = tag_number
        self.driver.TagType = 7
        self.driver.TagValueStr = tag_value
        self.driver.FNSendTagOperation()

    # def set_new_tags(self, summ_total):
    #     self.driver.TagNumber = 1011
    #     self.driver.TagType = 7
    #     self.driver.TagValueStr = 1
    #     self.driver.FNSendTagOperation()
    #
    #     self.driver.TagNumber = 1082
    #     self.driver.TagType = 7
    #     self.driver.TagValueStr = f'{summ_total}'
    #     self.driver.FNSendTagOperation()


class FiscalDriver(BaseFiscal):
    """Класс для управления ККТ."""

    def check_connection(self):
        """Проверка соединения с ККТ."""
        return self.driver.Connected

    def reset_ecr(self):
        """Сброс ККМ."""
        return self.driver.ResetECR()

    def get_ecr_status(self):
        """Запрос статуса ККТ."""
        return self.driver.GetECRStatus()

    def read_ecr_status(self):
        """Чтeние статуса ККТ."""
        return {
            'OperatorNumber': self.driver.OperatorNumber,
            'ECRSoftVersion': self.driver.ECRSoftVersion,
            'ECRBuild': self.driver.ECRBuild,
            'ECRSoftDate': str(self.driver.ECRSoftDate),
            'LogicalNumber': self.driver.LogicalNumber,
            'OpenDocumentNumber': self.driver.OpenDocumentNumber,
            'ECRFlags': self.driver.ECRFlags,
            'ReceiptRibbonIsPresent': self.driver.ReceiptRibbonIsPresent,
            'JournalRibbonIsPresent': self.driver.JournalRibbonIsPresent,
            'SKNOStatus': self.driver.SKNOStatus,
            'SlipDocumentIsPresent': self.driver.SlipDocumentIsPresent,
            'SlipDocumentIsMoving': self.driver.SlipDocumentIsMoving,
            'PointPosition': self.driver.PointPosition,
            'EKLZIsPresent': self.driver.EKLZIsPresent,
            'JournalRibbonOpticalSensor': self.driver.JournalRibbonOpticalSensor,
            'ReceiptRibbonOpticalSensor': self.driver.ReceiptRibbonOpticalSensor,
            'JournalRibbonLever': self.driver.JournalRibbonLever,
            'ReceiptRibbonLever': self.driver.ReceiptRibbonLever,
            'LidPositionSensor': self.driver.LidPositionSensor,
            'IsPrinterLeftSensorFailure': self.driver.IsPrinterLeftSensorFailure,
            'IsPrinterRightSensorFailure': self.driver.IsPrinterRightSensorFailure,
            'PresenterIn': self.driver.PresenterIn,
            'PresenterOut': self.driver.PresenterOut,
            'IsDrawerOpen': self.driver.IsDrawerOpen,
            'IsEKLZOverflow': self.driver.IsEKLZOverflow,
            'QuantityPointPosition': self.driver.QuantityPointPosition,
            'ECRMode': self.driver.ECRMode,
            'ECRModeDescription': self.driver.ECRModeDescription,
            'ECRMode8Status': self.driver.ECRMode8Status,
            'ECRModeStatus': self.driver.ECRModeStatus,
            'ECRAdvancedMode': self.driver.ECRAdvancedMode,
            'ECRAdvancedModeDescription': self.driver.ECRAdvancedModeDescription,
            'PortNumber': self.driver.PortNumber,
            'FMSoftVersion': self.driver.FMSoftVersion,
            'FMBuild': self.driver.FMBuild,
            'FMSoftDate': str(self.driver.FMSoftDate),
            'Date': str(self.driver.Date),
            'Time': str(self.driver.Time),
            'TimeStr': self.driver.TimeStr,
            'FMFlags': self.driver.FMFlags,
            'FM1IsPresent': self.driver.FM1IsPresent,
            'FM2IsPresent': self.driver.FM2IsPresent,
            'LicenseIsPresent': self.driver.LicenseIsPresent,
            'FMOverflow': self.driver.FMOverflow,
            'IsBatteryLow': self.driver.IsBatteryLow,
            'IsLastFMRecordCorrupted': self.driver.IsLastFMRecordCorrupted,
            'IsFMSessionOpen': self.driver.IsFMSessionOpen,
            'IsFM24HoursOver': self.driver.IsFM24HoursOver,
            'SerialNumber': self.driver.SerialNumber,
            'SessionNumber': self.driver.SessionNumber,
            'FreeRecordInFM': self.driver.FreeRecordInFM,
            'RegistrationNumber': self.driver.RegistrationNumber,
            'FreeRegistration': self.driver.FreeRegistration,
            'INN': self.driver.INN,
        }

    def print_string(self, string: str, font_number: int = 5):
        """Печать строки выбранным шрифтом."""
        self.driver.FontType = font_number
        self.driver.StringForPrinting = string
        return self.driver.PrintStringWithFont()

    def cut_check(self, full_cut: bool = True):
        """Отрезка чековой ленты."""
        self.driver.CutType = full_cut # False - полная отрезка
        self.driver.CutCheck()

    def change_is_printing(self, is_printing: bool):
        """Включение/отключение печати бумажного чека."""
        self.driver.DeviceFunctionNumber = self.driver.DFE_SkipAllPrinting
        self.driver.ValueOfFunctionInteger = 0 if is_printing else 1
        return self.driver.SetDeviceFunction()


driver = FiscalDriver()
fn = FiscalStorage()
