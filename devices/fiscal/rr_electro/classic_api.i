%module classic_fr_drv_ngx
%include <std_string.i>
%include <stdint.i>
%include <std_vector.i>
%pragma(java) moduleimports=%{
import java.util.Date;
%}
%pragma(java) jniclassimports=%{
import java.util.Date;
%}


#ifdef SWIGPYTHON
%{
#include <cstdint>
%}
// Instantiate templates used by classic_fr_drv_ngx
namespace std {
    %template(VectorOfBytes) vector<uint8_t>;
}
#endif //SWIGPYTHON

%{
#include <classic_api.h>
#include <chrono>

%}
#ifdef SWIGPYTHON
%{
#include <datetime.h>
%}

%typemap(out) std::time_t {
  if (!PyDateTimeAPI) { PyDateTime_IMPORT; }
  PyObject *floatObj = NULL;
  PyObject *timeTuple = NULL;
  floatObj = PyFloat_FromDouble(static_cast<double>($1));
  timeTuple = Py_BuildValue("(O)", floatObj);
  $result = PyDateTime_FromTimestamp(timeTuple);
}

%typemap(typecheck, precedence=SWIG_TYPECHECK_POINTER) std::time_t {
  if (!PyDateTimeAPI) { PyDateTime_IMPORT; }
  $1 = PyDateTime_Check($input) ? 1 : 0;
}

%typemap(in) std::time_t {
  if (!PyDateTimeAPI) { PyDateTime_IMPORT; }
  if (!PyDateTime_Check($input)) {
    PyErr_SetString(PyExc_ValueError,"Expected a datetime"); return NULL;
  }
    struct tm t ={
      PyDateTime_DATE_GET_SECOND($input),
      PyDateTime_DATE_GET_MINUTE($input),
      PyDateTime_DATE_GET_HOUR($input),
      PyDateTime_GET_DAY($input),
      PyDateTime_GET_MONTH($input)-1,
      PyDateTime_GET_YEAR($input)-1900,
      0,
      0,
      0
    };
  $1 = mktime(&t);
}
#endif //SWIGPYTHON

#ifdef SWIGJAVA


/* turn on director wrapping std::function<void(const std::string&)> */
%feature("director") std::function<void(const std::string&)>;
/* turn on director wrapping std::function<void(const std::string&)> */
%feature("director") (*const func)(const std::string&);
%typemap(javaimports) classic_interface
%{
import java.util.Date;
%}
%typemap(javacode) classic_interface
%{
static{
        System.loadLibrary("classic_fr_drv_ngx");
}
%}
// std::time_t
%typemap(jni) std::time_t "jobject"
%typemap(jtype) std::time_t "Date"
%typemap(jstype) std::time_t "Date"
%typemap(javadirectorin) std::time_t "$jniinput"
%typemap(javadirectorout) std::time_t "$javacall"

%typemap(in) std::time_t 
%{ if(!$input) {
     SWIG_JavaThrowException(jenv, SWIG_JavaNullPointerException, "null std::time_t");
     return $null;
    } 
    auto dateClass = jenv->GetObjectClass($input);
    auto getTimeId = jenv->GetMethodID(dateClass, "getTime", "()J");
    auto ret = jenv->CallLongMethod($input, getTimeId);
    $1 = static_cast<std::time_t>(ret / 1000);
%}

%typemap(out) std::time_t 
%{ 
 auto dateClass = jenv->FindClass("java/util/Date");
 auto dateTypeConstructor = jenv->GetMethodID(dateClass, "<init>", "(J)V");
 $result = jenv->NewObject(dateClass, dateTypeConstructor, static_cast<jlong>($1 * static_cast<jlong>(1000)));
%}

%typemap(javain) std::time_t "$javainput"

%typemap(javaout) std::time_t {
    return $jnicall;
  }
  
// std::vector<uint8_t>
%typemap(jni) std::vector<uint8_t> "jbyteArray"
%typemap(jtype) std::vector<uint8_t> "byte[]"
%typemap(jstype) std::vector<uint8_t> "byte[]"
%typemap(javadirectorin) std::vector<uint8_t> "$jniinput"
%typemap(javadirectorout) std::vector<uint8_t> "$javacall"

%typemap(in) std::vector<uint8_t> 
%{ if(!$input) {
     SWIG_JavaThrowException(jenv, SWIG_JavaNullPointerException, "null std::vector<uint8_t>");
     return $null;
    } 
    std::vector<uint8_t> result;
    auto bytesSize = jenv->GetArrayLength($input);
    if (bytesSize != 0) {
        result = std::vector<uint8_t> (static_cast<size_t>(bytesSize));
        $1 = &result;
        jenv->GetByteArrayRegion($input, 0, bytesSize, reinterpret_cast<jbyte*>(result.data()));
    }
%}

%typemap(out) std::vector<uint8_t> 
%{ 
    auto maxSize = $1.size();
    $result = jenv->NewByteArray(maxSize);
    jenv->SetByteArrayRegion(
                $result, 0, maxSize, reinterpret_cast<const signed char*>($1.data()));
%}

%typemap(javain) std::vector<uint8_t> "$javainput"

%typemap(javaout) std::vector<uint8_t> {
    return $jnicall;
  }
  
  // const std::vector<uint8_t> &
%typemap(jni) const std::vector<uint8_t> & "jbyteArray"
%typemap(jtype) const std::vector<uint8_t> & "byte[]"
%typemap(jstype) const std::vector<uint8_t> & "byte[]"
%typemap(javadirectorin) const std::vector<uint8_t> & "$jniinput"
%typemap(javadirectorout) const std::vector<uint8_t> & "$javacall"

%typemap(in) const std::vector<uint8_t> & 
%{ if(!$input) {
     SWIG_JavaThrowException(jenv, SWIG_JavaNullPointerException, "null std::vector<uint8_t> &");
     return $null;
    } 
    std::vector<uint8_t> result;
    auto bytesSize = jenv->GetArrayLength($input);
    if (bytesSize != 0) {
        result = std::vector<uint8_t> (static_cast<size_t>(bytesSize));
        $1 = &result;
        jenv->GetByteArrayRegion($input, 0, bytesSize, reinterpret_cast<jbyte*>(result.data()));
    }
%}

%typemap(out) const std::vector<uint8_t> & 
%{ 
    auto maxSize = $1.size();
    $result = jenv->NewByteArray(maxSize);
    jenv->SetByteArrayRegion(
                $result, 0, maxSize, reinterpret_cast<const signed char*>($1.data()));
%}

%typemap(javain) const std::vector<uint8_t> & "$javainput"

%typemap(javaout) const std::vector<uint8_t> & {
    return $jnicall;
  }
  
#endif //SWIGJAVA
#ifdef SWIGCSHARP

typedef long long int std::time_t;
%template(BytesVector) std::vector<uint8_t>;
%apply int64_t { std::time_t };
#endif //SWIGCSHARP


#ifdef SWIGLUA
%define LLDB_NUMBER_TYPEMAP(TYPE)
// Primitive integer mapping
%typemap(in,checkfn="lua_isinteger") TYPE
%{ $1 = ($type)lua_tointeger(L, $input); %}
%typemap(in,checkfn="lua_isinteger") const TYPE&($basetype temp)
%{ temp=($basetype)lua_tointeger(L,$input); $1=&temp;%}
%typemap(out) TYPE
%{ lua_pushinteger(L, (lua_Integer) $1); SWIG_arg++;%}
%typemap(out) const TYPE&
%{ lua_pushinteger(L, (lua_Integer) $1); SWIG_arg++;%}
// Pointer and reference mapping
%typemap(in,checkfn="lua_isinteger") TYPE *INPUT($*ltype temp), TYPE &INPUT($*ltype temp)
%{ temp = ($*ltype)lua_tointeger(L,$input);
   $1 = &temp; %}
%typemap(in, numinputs=0) TYPE *OUTPUT ($*ltype temp)
%{ $1 = &temp; %}
%typemap(argout) TYPE *OUTPUT
%{  lua_pushinteger(L, (lua_Integer) *$1); SWIG_arg++;%}
%typemap(in) TYPE *INOUT = TYPE *INPUT;
%typemap(argout) TYPE *INOUT = TYPE *OUTPUT;
%typemap(in) TYPE &OUTPUT = TYPE *OUTPUT;
%typemap(argout) TYPE &OUTPUT = TYPE *OUTPUT;
%typemap(in) TYPE &INOUT = TYPE *INPUT;
%typemap(argout) TYPE &INOUT = TYPE *OUTPUT;
%typemap(in,checkfn="lua_isinteger") const TYPE *INPUT($*ltype temp)
%{ temp = ($*ltype)lua_tointeger(L,$input);
   $1 = &temp; %}

%enddef // LLDB_NUMBER_TYPEMAP

LLDB_NUMBER_TYPEMAP(unsigned char);
LLDB_NUMBER_TYPEMAP(signed char);
LLDB_NUMBER_TYPEMAP(short);
LLDB_NUMBER_TYPEMAP(unsigned short);
LLDB_NUMBER_TYPEMAP(signed short);
LLDB_NUMBER_TYPEMAP(int);
LLDB_NUMBER_TYPEMAP(unsigned int);
LLDB_NUMBER_TYPEMAP(signed int);
LLDB_NUMBER_TYPEMAP(long);
LLDB_NUMBER_TYPEMAP(unsigned long);
LLDB_NUMBER_TYPEMAP(signed long);
LLDB_NUMBER_TYPEMAP(long long);
LLDB_NUMBER_TYPEMAP(unsigned long long);
LLDB_NUMBER_TYPEMAP(signed long long);
LLDB_NUMBER_TYPEMAP(enum SWIGTYPE);
LLDB_NUMBER_TYPEMAP(std::time_t);
LLDB_NUMBER_TYPEMAP(time_t);

%apply unsigned long { size_t };
%apply const unsigned long & { const size_t & };
%apply long { ssize_t };
%apply const long & { const ssize_t & };


%{
#include <cstdint>
using namespace kkt_driver;
%}
namespace std {
    %template(VectorOfBytes) vector<uint8_t>;
}


#endif //SWIGLUA

#if defined(SWIGPYTHON) || defined (SWIGCSHARP) || defined(SWIGLUA)
%include <attribute.i>
%attribute(kkt_driver::classic_interface, int, ActivizationControlByte, Get_ActivizationControlByte, Set_ActivizationControlByte);
%attribute(kkt_driver::classic_interface, int, ActivizationStatus, Get_ActivizationStatus, Set_ActivizationStatus);
%attribute(kkt_driver::classic_interface, bool, AdjustRITimeout, Get_AdjustRITimeout, Set_AdjustRITimeout);
%attribute(kkt_driver::classic_interface, int, AnswerCode, Get_AnswerCode, Set_AnswerCode);
%attribute(kkt_driver::classic_interface, int, AttributeNumber, Get_AttributeNumber, Set_AttributeNumber);
%attributestring(kkt_driver::classic_interface, std::string, AttributeValue, Get_AttributeValue, Set_AttributeValue);
%attribute(kkt_driver::classic_interface, bool, AutoSensorValues, Get_AutoSensorValues, Set_AutoSensorValues);
%attribute(kkt_driver::classic_interface, bool, AutoStartSearch, Get_AutoStartSearch, Set_AutoStartSearch);
%attribute(kkt_driver::classic_interface, int, BanknoteCount, Get_BanknoteCount);
%attribute(kkt_driver::classic_interface, int, BanknoteType, Get_BanknoteType);
%attributestring(kkt_driver::classic_interface, std::string, BarCode, Get_BarCode, Set_BarCode);
%attribute(kkt_driver::classic_interface, TBarcodeAlignment, BarcodeAlignment, Get_BarcodeAlignment, Set_BarcodeAlignment);
%attribute(kkt_driver::classic_interface, int, BarcodeDataLength, Get_BarcodeDataLength, Set_BarcodeDataLength);
%attribute(kkt_driver::classic_interface, int, BarcodeFirstLine, Get_BarcodeFirstLine, Set_BarcodeFirstLine);
%attributestring(kkt_driver::classic_interface, std::string, BarcodeHex, Get_BarcodeHex, Set_BarcodeHex);
%attribute(kkt_driver::classic_interface, int, BarcodeParameter1, Get_BarcodeParameter1, Set_BarcodeParameter1);
%attribute(kkt_driver::classic_interface, int, BarcodeParameter2, Get_BarcodeParameter2, Set_BarcodeParameter2);
%attribute(kkt_driver::classic_interface, int, BarcodeParameter3, Get_BarcodeParameter3, Set_BarcodeParameter3);
%attribute(kkt_driver::classic_interface, int, BarcodeParameter4, Get_BarcodeParameter4, Set_BarcodeParameter4);
%attribute(kkt_driver::classic_interface, int, BarcodeParameter5, Get_BarcodeParameter5, Set_BarcodeParameter5);
%attribute(kkt_driver::classic_interface, int, BarcodeStartBlockNumber, Get_BarcodeStartBlockNumber, Set_BarcodeStartBlockNumber);
%attribute(kkt_driver::classic_interface, int, BarcodeType, Get_BarcodeType, Set_BarcodeType);
%attribute(kkt_driver::classic_interface, int, BarWidth, Get_BarWidth, Set_BarWidth);
%attribute(kkt_driver::classic_interface, double, BatteryVoltage, Get_BatteryVoltage);
%attribute(kkt_driver::classic_interface, int, BaudRate, Get_BaudRate, Set_BaudRate);
%attribute(kkt_driver::classic_interface, TBinaryConversion, BinaryConversion, Get_BinaryConversion, Set_BinaryConversion);
%attributeval(kkt_driver::classic_interface, std::vector<uint8_t>, BlockData, Get_BlockData, Set_BlockData);
%attributestring(kkt_driver::classic_interface, std::string, BlockDataHex, Get_BlockDataHex, Set_BlockDataHex);
%attribute(kkt_driver::classic_interface, int, BlockNumber, Get_BlockNumber, Set_BlockNumber);
%attribute(kkt_driver::classic_interface, int, BlockType, Get_BlockType, Set_BlockType);
%attribute(kkt_driver::classic_interface, int, BufferingType, Get_BufferingType, Set_BufferingType);
%attribute(kkt_driver::classic_interface, int, CalculationSign, Get_CalculationSign, Set_CalculationSign);
%attribute(kkt_driver::classic_interface, bool, CapGetShortECRStatus, Get_CapGetShortECRStatus);
%attribute(kkt_driver::classic_interface, bool, CarryStrings, Get_CarryStrings, Set_CarryStrings);
%attribute(kkt_driver::classic_interface, int, CashAcceptorPollingMode, Get_CashAcceptorPollingMode);
%attribute(kkt_driver::classic_interface, bool, CashControlEnabled, Get_CashControlEnabled, Set_CashControlEnabled);
%attributestring(kkt_driver::classic_interface, std::string, CashControlHost, Get_CashControlHost, Set_CashControlHost);
%attribute(kkt_driver::classic_interface, int, CashControlPassword, Get_CashControlPassword, Set_CashControlPassword);
%attributestring(kkt_driver::classic_interface, std::string, CashControlPort, Get_CashControlPort, Set_CashControlPort);
%attributestring(kkt_driver::classic_interface, std::string, CashControlProtocols, Get_CashControlProtocols);
%attribute(kkt_driver::classic_interface, bool, CashControlUseTCP, Get_CashControlUseTCP, Set_CashControlUseTCP);
%attribute(kkt_driver::classic_interface, int, ccHeaderLineCount, Get_ccHeaderLineCount, Set_ccHeaderLineCount);
%attribute(kkt_driver::classic_interface, bool, ccUseTextAsWareName, Get_ccUseTextAsWareName, Set_ccUseTextAsWareName);
%attribute(kkt_driver::classic_interface, int, ccWareNameLineNumber, Get_ccWareNameLineNumber, Set_ccWareNameLineNumber);
%attribute(kkt_driver::classic_interface, bool, CenterImage, Get_CenterImage, Set_CenterImage);
%attribute(kkt_driver::classic_interface, int64_t, Change, Get_Change);
%attribute(kkt_driver::classic_interface, int, ChangeFont, Get_ChangeFont, Set_ChangeFont);
%attribute(kkt_driver::classic_interface, int, ChangeOffset, Get_ChangeOffset, Set_ChangeOffset);
%attribute(kkt_driver::classic_interface, int, ChangeStringNumber, Get_ChangeStringNumber, Set_ChangeStringNumber);
%attribute(kkt_driver::classic_interface, int, ChangeSumFont, Get_ChangeSumFont, Set_ChangeSumFont);
%attribute(kkt_driver::classic_interface, int, ChangeSumOffset, Get_ChangeSumOffset, Set_ChangeSumOffset);
%attribute(kkt_driver::classic_interface, int, ChangeSymbolNumber, Get_ChangeSymbolNumber, Set_ChangeSymbolNumber);
%attribute(kkt_driver::classic_interface, int64_t, ChargeValue, Get_ChargeValue, Set_ChargeValue);
%attribute(kkt_driver::classic_interface, int, CharHeight, Get_CharHeight);
%attribute(kkt_driver::classic_interface, int, CharWidth, Get_CharWidth);
%attribute(kkt_driver::classic_interface, bool, CheckEJConnection, Get_CheckEJConnection, Set_CheckEJConnection);
%attribute(kkt_driver::classic_interface, bool, CheckFMConnection, Get_CheckFMConnection, Set_CheckFMConnection);
%attribute(kkt_driver::classic_interface, int, CheckingType, Get_CheckingType, Set_CheckingType);
%attribute(kkt_driver::classic_interface, int, CheckType, Get_CheckType, Set_CheckType);
%attributestring(kkt_driver::classic_interface, std::string, ConnectionURI, Get_ConnectionURI, Set_ConnectionURI);
%attribute(kkt_driver::classic_interface, int, ClicheFont, Get_ClicheFont, Set_ClicheFont);
%attribute(kkt_driver::classic_interface, int, ClicheOffset, Get_ClicheOffset, Set_ClicheOffset);
%attribute(kkt_driver::classic_interface, int, ClicheStringNumber, Get_ClicheStringNumber, Set_ClicheStringNumber);
%attribute(kkt_driver::classic_interface, bool, CloudCashdeskEnabled, Get_CloudCashdeskEnabled, Set_CloudCashdeskEnabled);
%attribute(kkt_driver::classic_interface, TCodePage, CodePage, Get_CodePage, Set_CodePage);
%attribute(kkt_driver::classic_interface, int, CommandCode, Get_CommandCode);
%attribute(kkt_driver::classic_interface, int, CommandCount, Get_CommandCount);
%attribute(kkt_driver::classic_interface, int, CommandDefTimeout, Get_CommandDefTimeout);
%attribute(kkt_driver::classic_interface, int, CommandIndex, Get_CommandIndex, Set_CommandIndex);
%attributestring(kkt_driver::classic_interface, std::string, CommandName, Get_CommandName);
%attribute(kkt_driver::classic_interface, int, CommandRetryCount, Get_CommandRetryCount, Set_CommandRetryCount);
%attribute(kkt_driver::classic_interface, int, CommandTimeout, Get_CommandTimeout, Set_CommandTimeout);
%attribute(kkt_driver::classic_interface, int, ComNumber, Get_ComNumber, Set_ComNumber);
%attributestring(kkt_driver::classic_interface, std::string, ComputerName, Get_ComputerName, Set_ComputerName);
%attribute(kkt_driver::classic_interface, bool, Connected, Get_Connected, Set_Connected);
%attribute(kkt_driver::classic_interface, int, ConnectionTimeout, Get_ConnectionTimeout, Set_ConnectionTimeout);
%attribute(kkt_driver::classic_interface, TConnectionType, ConnectionType, Get_ConnectionType, Set_ConnectionType);
%attribute(kkt_driver::classic_interface, int64_t, ContentsOfCashRegister, Get_ContentsOfCashRegister);
%attribute(kkt_driver::classic_interface, int, ContentsOfOperationRegister, Get_ContentsOfOperationRegister);
%attribute(kkt_driver::classic_interface, int, CopyOffset1, Get_CopyOffset1, Set_CopyOffset1);
%attribute(kkt_driver::classic_interface, int, CopyOffset2, Get_CopyOffset2, Set_CopyOffset2);
%attribute(kkt_driver::classic_interface, int, CopyOffset3, Get_CopyOffset3, Set_CopyOffset3);
%attribute(kkt_driver::classic_interface, int, CopyOffset4, Get_CopyOffset4, Set_CopyOffset4);
%attribute(kkt_driver::classic_interface, int, CopyOffset5, Get_CopyOffset5, Set_CopyOffset5);
%attribute(kkt_driver::classic_interface, int, CopyType, Get_CopyType, Set_CopyType);
%attribute(kkt_driver::classic_interface, int, CorrectionType, Get_CorrectionType, Set_CorrectionType);
%attribute(kkt_driver::classic_interface, int, CustomerCode, Get_CustomerCode, Set_CustomerCode);
%attributestring(kkt_driver::classic_interface, std::string, CustomerEmail, Get_CustomerEmail, Set_CustomerEmail);
%attribute(kkt_driver::classic_interface, bool, CutType, Get_CutType, Set_CutType);
%attributestring(kkt_driver::classic_interface, std::string, DataBlock, Get_DataBlock);
%attribute(kkt_driver::classic_interface, int, DataBlockNumber, Get_DataBlockNumber);
%attribute(kkt_driver::classic_interface, int, DataLength, Get_DataLength, Set_DataLength);
%attribute(kkt_driver::classic_interface, std::time_t, Date, Get_Date, Set_Date);
%attribute(kkt_driver::classic_interface, std::time_t, Date2, Get_Date2, Set_Date2);
%attribute(kkt_driver::classic_interface, int, DBDocType, Get_DBDocType, Set_DBDocType);
%attributestring(kkt_driver::classic_interface, std::string, DBFilePath, Get_DBFilePath, Set_DBFilePath);
%attribute(kkt_driver::classic_interface, bool, DelayedPrint, Get_DelayedPrint, Set_DelayedPrint);
%attribute(kkt_driver::classic_interface, int, Department, Get_Department, Set_Department);
%attribute(kkt_driver::classic_interface, int, DepartmentFont, Get_DepartmentFont, Set_DepartmentFont);
%attribute(kkt_driver::classic_interface, int, DepartmentOffset, Get_DepartmentOffset, Set_DepartmentOffset);
%attribute(kkt_driver::classic_interface, int, DepartmentStringNumber, Get_DepartmentStringNumber, Set_DepartmentStringNumber);
%attribute(kkt_driver::classic_interface, int, DepartmentSymbolNumber, Get_DepartmentSymbolNumber, Set_DepartmentSymbolNumber);
%attribute(kkt_driver::classic_interface, int, DeviceCode, Get_DeviceCode, Set_DeviceCode);
%attributestring(kkt_driver::classic_interface, std::string, DeviceCodeDescription, Get_DeviceCodeDescription);
%attribute(kkt_driver::classic_interface, int64_t, Discount1, Get_Discount1, Set_Discount1);
%attribute(kkt_driver::classic_interface, int64_t, Discount2, Get_Discount2, Set_Discount2);
%attribute(kkt_driver::classic_interface, int64_t, Discount3, Get_Discount3, Set_Discount3);
%attribute(kkt_driver::classic_interface, int64_t, Discount4, Get_Discount4, Set_Discount4);
%attribute(kkt_driver::classic_interface, double, DiscountOnCheck, Get_DiscountOnCheck,Set_DiscountOnCheck);
%attribute(kkt_driver::classic_interface, int, DiscountOnCheckFont, Get_DiscountOnCheckFont, Set_DiscountOnCheckFont);
%attribute(kkt_driver::classic_interface, int, DiscountOnCheckOffset, Get_DiscountOnCheckOffset, Set_DiscountOnCheckOffset);
%attribute(kkt_driver::classic_interface, int, DiscountOnCheckStringNumber, Get_DiscountOnCheckStringNumber, Set_DiscountOnCheckStringNumber);
%attribute(kkt_driver::classic_interface, int, DiscountOnCheckSumFont, Get_DiscountOnCheckSumFont, Set_DiscountOnCheckSumFont);
%attribute(kkt_driver::classic_interface, int, DiscountOnCheckSumOffset, Get_DiscountOnCheckSumOffset, Set_DiscountOnCheckSumOffset);
%attribute(kkt_driver::classic_interface, int, DiscountOnCheckSumSymbolNumber, Get_DiscountOnCheckSumSymbolNumber, Set_DiscountOnCheckSumSymbolNumber);
%attribute(kkt_driver::classic_interface, int, DiscountOnCheckSymbolNumber, Get_DiscountOnCheckSymbolNumber, Set_DiscountOnCheckSymbolNumber);
%attribute(kkt_driver::classic_interface, int64_t, DiscountValue, Get_DiscountValue, Set_DiscountValue);
%attribute(kkt_driver::classic_interface, int, DocumentCount, Get_DocumentCount, Set_DocumentCount);
%attributestring(kkt_driver::classic_interface, std::string, DocumentName, Get_DocumentName, Set_DocumentName);
%attribute(kkt_driver::classic_interface, int, DocumentNumber, Get_DocumentNumber, Set_DocumentNumber);
%attribute(kkt_driver::classic_interface, int, DocumentType, Get_DocumentType, Set_DocumentType);
%attribute(kkt_driver::classic_interface, bool, DoNotSendENQ, Get_DoNotSendENQ, Set_DoNotSendENQ);
%attribute(kkt_driver::classic_interface, int, DrawerNumber, Get_DrawerNumber, Set_DrawerNumber);
%attribute(kkt_driver::classic_interface, int, DriverBuild, Get_DriverBuild);
%attribute(kkt_driver::classic_interface, int, DriverMajorVersion, Get_DriverMajorVersion);
%attribute(kkt_driver::classic_interface, int, DriverMinorVersion, Get_DriverMinorVersion);
%attribute(kkt_driver::classic_interface, int, DriverRelease, Get_DriverRelease);
%attributestring(kkt_driver::classic_interface, std::string, DriverVersion, Get_DriverVersion);
%attribute(kkt_driver::classic_interface, int, ECRAdvancedMode, Get_ECRAdvancedMode);
%attributestring(kkt_driver::classic_interface, std::string, ECRAdvancedModeDescription, Get_ECRAdvancedModeDescription);
%attribute(kkt_driver::classic_interface, int, ECRBuild, Get_ECRBuild);
%attribute(kkt_driver::classic_interface, std::time_t, ECRDate, Get_ECRDate, Set_ECRDate);
%attribute(kkt_driver::classic_interface, int, ECRFlags, Get_ECRFlags);
%attributestring(kkt_driver::classic_interface, std::string, ECRID, Get_ECRID, Set_ECRID);
%attributestring(kkt_driver::classic_interface, std::string, ECRInput, Get_ECRInput);
%attribute(kkt_driver::classic_interface, int, ECRMode, Get_ECRMode);
%attribute(kkt_driver::classic_interface, int, ECRMode8Status, Get_ECRMode8Status);
%attributestring(kkt_driver::classic_interface, std::string, ECRModeDescription, Get_ECRModeDescription);
%attribute(kkt_driver::classic_interface, int, ECRModeStatus, Get_ECRModeStatus);
%attributestring(kkt_driver::classic_interface, std::string, ECROutput, Get_ECROutput);
%attribute(kkt_driver::classic_interface, std::time_t, ECRSoftDate, Get_ECRSoftDate);
%attributestring(kkt_driver::classic_interface, std::string, ECRSoftVersion, Get_ECRSoftVersion);
%attribute(kkt_driver::classic_interface, std::time_t, ECRTime, Get_ECRTime, Set_ECRTime);
%attribute(kkt_driver::classic_interface, int, EjectDirection, Get_EjectDirection, Set_EjectDirection);
%attributestring(kkt_driver::classic_interface, std::string, EKLZData, Get_EKLZData);
%attribute(kkt_driver::classic_interface, int, EKLZFlags, Get_EKLZFlags);
%attribute(kkt_driver::classic_interface, int, EKLZFont, Get_EKLZFont, Set_EKLZFont);
%attribute(kkt_driver::classic_interface, bool, EKLZIsPresent, Get_EKLZIsPresent);
%attributestring(kkt_driver::classic_interface, std::string, EKLZNumber, Get_EKLZNumber);
%attribute(kkt_driver::classic_interface, int, EKLZOffset, Get_EKLZOffset, Set_EKLZOffset);
%attribute(kkt_driver::classic_interface, int, EKLZResultCode, Get_EKLZResultCode);
%attribute(kkt_driver::classic_interface, int, EKLZStringNumber, Get_EKLZStringNumber, Set_EKLZStringNumber);
%attributestring(kkt_driver::classic_interface, std::string, EKLZVersion, Get_EKLZVersion);
%attribute(kkt_driver::classic_interface, int, ErrorCode, Get_ErrorCode, Set_ErrorCode);
%attributestring(kkt_driver::classic_interface, std::string, ErrorDescription, Get_ErrorDescription);
%attributestring(kkt_driver::classic_interface, std::string, EscapeIP, Get_EscapeIP, Set_EscapeIP);
%attribute(kkt_driver::classic_interface, int, EscapePort, Get_EscapePort, Set_EscapePort);
%attribute(kkt_driver::classic_interface, int, EscapeTimeout, Get_EscapeTimeout, Set_EscapeTimeout);
%attribute(kkt_driver::classic_interface, int, ExciseCode, Get_ExciseCode, Set_ExciseCode);
%attribute(kkt_driver::classic_interface, bool, FeedAfterCut, Get_FeedAfterCut, Set_FeedAfterCut);
%attribute(kkt_driver::classic_interface, int, FeedLineCount, Get_FeedLineCount, Set_FeedLineCount);
%attributestring(kkt_driver::classic_interface, std::string, FieldName, Get_FieldName);
%attribute(kkt_driver::classic_interface, int, FieldNumber, Get_FieldNumber, Set_FieldNumber);
%attribute(kkt_driver::classic_interface, int, FieldSize, Get_FieldSize);
%attribute(kkt_driver::classic_interface, bool, FieldType, Get_FieldType);
%attributestring(kkt_driver::classic_interface, std::string, FileName, Get_FileName, Set_FileName);
%attribute(kkt_driver::classic_interface, TFinishDocumentMode, FinishDocumentMode, Get_FinishDocumentMode, Set_FinishDocumentMode);
%attribute(kkt_driver::classic_interface, int, FirstLineNumber, Get_FirstLineNumber, Set_FirstLineNumber);
%attribute(kkt_driver::classic_interface, std::time_t, FirstSessionDate, Get_FirstSessionDate, Set_FirstSessionDate);
%attribute(kkt_driver::classic_interface, int, FirstSessionNumber, Get_FirstSessionNumber, Set_FirstSessionNumber);
%attribute(kkt_driver::classic_interface, int, FiscalSign, Get_FiscalSign, Set_FiscalSign);
%attributestring(kkt_driver::classic_interface, std::string, FiscalSignAsString, Get_FiscalSignAsString);
%attributestring(kkt_driver::classic_interface, std::string, FiscalSignOFD, Get_FiscalSignOFD, Set_FiscalSignOFD);
%attribute(kkt_driver::classic_interface, bool, FM1IsPresent, Get_FM1IsPresent);
%attribute(kkt_driver::classic_interface, bool, FM2IsPresent, Get_FM2IsPresent);
%attribute(kkt_driver::classic_interface, int, FMBuild, Get_FMBuild);
%attribute(kkt_driver::classic_interface, int, FMFlags, Get_FMFlags);
%attribute(kkt_driver::classic_interface, int, FMFlagsEx, Get_FMFlagsEx);
%attribute(kkt_driver::classic_interface, int, FMMode, Get_FMMode);
%attribute(kkt_driver::classic_interface, int, FMOffset, Get_FMOffset, Set_FMOffset);
%attribute(kkt_driver::classic_interface, bool, FMOverflow, Get_FMOverflow);
%attribute(kkt_driver::classic_interface, int, FMResultCode, Get_FMResultCode);
%attribute(kkt_driver::classic_interface, std::time_t, FMSoftDate, Get_FMSoftDate);
%attributestring(kkt_driver::classic_interface, std::string, FMSoftVersion, Get_FMSoftVersion);
%attribute(kkt_driver::classic_interface, int, FMStringNumber, Get_FMStringNumber, Set_FMStringNumber);
%attribute(kkt_driver::classic_interface, int, FNCurrentDocument, Get_FNCurrentDocument, Set_FNCurrentDocument);
%attribute(kkt_driver::classic_interface, int, FNDocumentData, Get_FNDocumentData);
%attribute(kkt_driver::classic_interface, int, FNLifeState, Get_FNLifeState);
%attribute(kkt_driver::classic_interface, int, FNSessionState, Get_FNSessionState);
%attribute(kkt_driver::classic_interface, int, FNSoftType, Get_FNSoftType);
%attributestring(kkt_driver::classic_interface, std::string, FNSoftVersion, Get_FNSoftVersion);
%attribute(kkt_driver::classic_interface, int, FNWarningFlags, Get_FNWarningFlags);
%attribute(kkt_driver::classic_interface, int, FontCount, Get_FontCount);
%attribute(kkt_driver::classic_interface, int, FontType, Get_FontType, Set_FontType);
%attribute(kkt_driver::classic_interface, int, FreeRecordInFM, Get_FreeRecordInFM);
%attribute(kkt_driver::classic_interface, int, FreeRegistration, Get_FreeRegistration);
%attribute(kkt_driver::classic_interface, int, HeaderFont, Get_HeaderFont, Set_HeaderFont);
%attribute(kkt_driver::classic_interface, int, HeaderOffset, Get_HeaderOffset, Set_HeaderOffset);
%attribute(kkt_driver::classic_interface, int, HeaderStringNumber, Get_HeaderStringNumber, Set_HeaderStringNumber);
%attribute(kkt_driver::classic_interface, int, HorizScale, Get_HorizScale, Set_HorizScale);
%attribute(kkt_driver::classic_interface, int, HRIPosition, Get_HRIPosition, Set_HRIPosition);
%attribute(kkt_driver::classic_interface, int, IBMDocumentNumber, Get_IBMDocumentNumber);
%attribute(kkt_driver::classic_interface, int, IBMFlags, Get_IBMFlags);
%attribute(kkt_driver::classic_interface, int, IBMLastBuyReceiptNumber, Get_IBMLastBuyReceiptNumber);
%attribute(kkt_driver::classic_interface, int, IBMLastReturnBuyReceiptNumber, Get_IBMLastReturnBuyReceiptNumber);
%attribute(kkt_driver::classic_interface, int, IBMLastReturnSaleReceiptNumber, Get_IBMLastReturnSaleReceiptNumber);
%attribute(kkt_driver::classic_interface, int, IBMLastSaleReceiptNumber, Get_IBMLastSaleReceiptNumber);
%attribute(kkt_driver::classic_interface, std::time_t, IBMSessionDateTime, Get_IBMSessionDateTime);
%attribute(kkt_driver::classic_interface, int, IBMSessionDay, Get_IBMSessionDay);
%attribute(kkt_driver::classic_interface, int, IBMSessionHour, Get_IBMSessionHour);
%attribute(kkt_driver::classic_interface, int, IBMSessionMin, Get_IBMSessionMin);
%attribute(kkt_driver::classic_interface, int, IBMSessionMonth, Get_IBMSessionMonth);
%attribute(kkt_driver::classic_interface, int, IBMSessionSec, Get_IBMSessionSec);
%attribute(kkt_driver::classic_interface, int, IBMSessionYear, Get_IBMSessionYear);
%attribute(kkt_driver::classic_interface, int, IBMStatusByte1, Get_IBMStatusByte1);
%attribute(kkt_driver::classic_interface, int, IBMStatusByte2, Get_IBMStatusByte2);
%attribute(kkt_driver::classic_interface, int, IBMStatusByte3, Get_IBMStatusByte3);
%attribute(kkt_driver::classic_interface, int, IBMStatusByte4, Get_IBMStatusByte4);
%attribute(kkt_driver::classic_interface, int, IBMStatusByte5, Get_IBMStatusByte5);
%attribute(kkt_driver::classic_interface, int, IBMStatusByte6, Get_IBMStatusByte6);
%attribute(kkt_driver::classic_interface, int, IBMStatusByte7, Get_IBMStatusByte7);
%attribute(kkt_driver::classic_interface, int, IBMStatusByte8, Get_IBMStatusByte8);
%attribute(kkt_driver::classic_interface, int, InfoExchangeStatus, Get_InfoExchangeStatus, Set_InfoExchangeStatus);
%attribute(kkt_driver::classic_interface, int, InfoType, Get_InfoType, Set_InfoType);
%attributestring(kkt_driver::classic_interface, std::string, INN, Get_INN, Set_INN);
%attribute(kkt_driver::classic_interface, int, INNAsInteger, Get_INNAsInteger);
%attribute(kkt_driver::classic_interface, int, IntervalNumber, Get_IntervalNumber, Set_IntervalNumber);
%attribute(kkt_driver::classic_interface, int, IntervalValue, Get_IntervalValue, Set_IntervalValue);
%attributestring(kkt_driver::classic_interface, std::string, IPAddress, Get_IPAddress, Set_IPAddress);
%attribute(kkt_driver::classic_interface, bool, IsASPDMode, Get_IsASPDMode);
%attribute(kkt_driver::classic_interface, bool, IsBatteryLow, Get_IsBatteryLow);
%attribute(kkt_driver::classic_interface, bool, IsBlockedByWrongTaxPassword, Get_IsBlockedByWrongTaxPassword);
%attribute(kkt_driver::classic_interface, bool, IsClearUnfiscalInfo, Get_IsClearUnfiscalInfo, Set_IsClearUnfiscalInfo);
%attribute(kkt_driver::classic_interface, bool, IsCorruptedFiscalizationInfo, Get_IsCorruptedFiscalizationInfo);
%attribute(kkt_driver::classic_interface, bool, IsCorruptedFMRecords, Get_IsCorruptedFMRecords);
%attribute(kkt_driver::classic_interface, bool, IsDrawerOpen, Get_IsDrawerOpen);
%attribute(kkt_driver::classic_interface, bool, IsEKLZOverflow, Get_IsEKLZOverflow);
%attribute(kkt_driver::classic_interface, bool, IsFM24HoursOver, Get_IsFM24HoursOver);
%attribute(kkt_driver::classic_interface, bool, IsFMSessionOpen, Get_IsFMSessionOpen);
%attribute(kkt_driver::classic_interface, bool, IsLastFMRecordCorrupted, Get_IsLastFMRecordCorrupted);
%attribute(kkt_driver::classic_interface, bool, IsPrinterLeftSensorFailure, Get_IsPrinterLeftSensorFailure);
%attribute(kkt_driver::classic_interface, bool, IsPrinterRightSensorFailure, Get_IsPrinterRightSensorFailure);
%attribute(kkt_driver::classic_interface, bool, JournalEnabled, Get_JournalEnabled, Set_JournalEnabled);
%attribute(kkt_driver::classic_interface, bool, JournalRibbonIsPresent, Get_JournalRibbonIsPresent);
%attribute(kkt_driver::classic_interface, bool, JournalRibbonLever, Get_JournalRibbonLever);
%attribute(kkt_driver::classic_interface, bool, JournalRibbonOpticalSensor, Get_JournalRibbonOpticalSensor);
%attributestring(kkt_driver::classic_interface, std::string, JournalRow, Get_JournalRow);
%attribute(kkt_driver::classic_interface, int, JournalRowCount, Get_JournalRowCount);
%attribute(kkt_driver::classic_interface, int, JournalRowNumber, Get_JournalRowNumber, Set_JournalRowNumber);
%attributestring(kkt_driver::classic_interface, std::string, JournalText, Get_JournalText);
%attributestring(kkt_driver::classic_interface, std::string, KKTRegistrationNumber, Get_KKTRegistrationNumber, Set_KKTRegistrationNumber);
%attribute(kkt_driver::classic_interface, int, KPKFont, Get_KPKFont, Set_KPKFont);
%attribute(kkt_driver::classic_interface, int, KPKNumber, Get_KPKNumber, Set_KPKNumber);
%attribute(kkt_driver::classic_interface, int, KPKOffset, Get_KPKOffset, Set_KPKOffset);
%attributestring(kkt_driver::classic_interface, std::string, KPKStr, Get_KPKStr);
%attribute(kkt_driver::classic_interface, int, KPKValue, Get_KPKValue, Set_KPKValue);
%attributestring(kkt_driver::classic_interface, std::string, KSAInfo, Get_KSAInfo, Set_KSAInfo);
%attribute(kkt_driver::classic_interface, int, LastFMRecordType, Get_LastFMRecordType);
%attribute(kkt_driver::classic_interface, std::time_t, LastKPKDate, Get_LastKPKDate);
%attributestring(kkt_driver::classic_interface, std::string, LastKPKDateStr, Get_LastKPKDateStr);
%attribute(kkt_driver::classic_interface, int64_t, LastKPKDocumentResult, Get_LastKPKDocumentResult);
%attribute(kkt_driver::classic_interface, int, LastKPKNumber, Get_LastKPKNumber);
%attribute(kkt_driver::classic_interface, std::time_t, LastKPKTime, Get_LastKPKTime);
%attributestring(kkt_driver::classic_interface, std::string, LastKPKTimeStr, Get_LastKPKTimeStr);
%attribute(kkt_driver::classic_interface, int, LastLineNumber, Get_LastLineNumber, Set_LastLineNumber);
%attribute(kkt_driver::classic_interface, int, LastPrintResult, Get_LastPrintResult);
%attribute(kkt_driver::classic_interface, std::time_t, LastSessionDate, Get_LastSessionDate, Set_LastSessionDate);
%attribute(kkt_driver::classic_interface, int, LastSessionNumber, Get_LastSessionNumber, Set_LastSessionNumber);
%attribute(kkt_driver::classic_interface, int, LDBaudrate, Get_LDBaudrate, Set_LDBaudrate);
%attribute(kkt_driver::classic_interface, int, LDComNumber, Get_LDComNumber, Set_LDComNumber);
%attributestring(kkt_driver::classic_interface, std::string, LDComputerName, Get_LDComputerName, Set_LDComputerName);
%attribute(kkt_driver::classic_interface, TConnectionType, LDConnectionType, Get_LDConnectionType, Set_LDConnectionType);
%attribute(kkt_driver::classic_interface, int, LDCount, Get_LDCount);
%attributestring(kkt_driver::classic_interface, std::string, LDEscapeIP, Get_LDEscapeIP, Set_LDEscapeIP);
%attribute(kkt_driver::classic_interface, int, LDEscapePort, Get_LDEscapePort, Set_LDEscapePort);
%attribute(kkt_driver::classic_interface, int, LDEscapeTimeout, Get_LDEscapeTimeout, Set_LDEscapeTimeout);
%attribute(kkt_driver::classic_interface, int, LDIndex, Get_LDIndex, Set_LDIndex);
%attributestring(kkt_driver::classic_interface, std::string, LDIPAddress, Get_LDIPAddress, Set_LDIPAddress);
%attributestring(kkt_driver::classic_interface, std::string, LDName, Get_LDName, Set_LDName);
%attribute(kkt_driver::classic_interface, int, LDNumber, Get_LDNumber, Set_LDNumber);
%attribute(kkt_driver::classic_interface, int, LDProtocolType, Get_LDProtocolType, Set_LDProtocolType);
%attribute(kkt_driver::classic_interface, int, LDSysAdminPassword, Get_LDSysAdminPassword, Set_LDSysAdminPassword);
%attribute(kkt_driver::classic_interface, int, LDTCPPort, Get_LDTCPPort, Set_LDTCPPort);
%attribute(kkt_driver::classic_interface, int, LDTimeout, Get_LDTimeout, Set_LDTimeout);
%attribute(kkt_driver::classic_interface, bool, LDUseIPAddress, Get_LDUseIPAddress, Set_LDUseIPAddress);
%attributestring(kkt_driver::classic_interface, std::string, License, Get_License, Set_License);
%attribute(kkt_driver::classic_interface, bool, LicenseIsPresent, Get_LicenseIsPresent);
%attribute(kkt_driver::classic_interface, bool, LidPositionSensor, Get_LidPositionSensor);
%attributestring(kkt_driver::classic_interface, std::string, LineData, Get_LineData, Set_LineData);
%attributestring(kkt_driver::classic_interface, std::string, LineData2, Get_LineData2, Set_LineData2);
%attributestring(kkt_driver::classic_interface, std::string, LineDataHex, Get_LineDataHex, Set_LineDataHex);
%attribute(kkt_driver::classic_interface, int, LineNumber, Get_LineNumber, Set_LineNumber);
%attribute(kkt_driver::classic_interface, bool, LineSwapBytes, Get_LineSwapBytes, Set_LineSwapBytes);
%attribute(kkt_driver::classic_interface, int, LockTimeout, Get_LockTimeout, Set_LockTimeout);
%attribute(kkt_driver::classic_interface, int, LogicalNumber, Get_LogicalNumber);
%attribute(kkt_driver::classic_interface, int, LogMaxFileCount, Get_LogMaxFileCount, Set_LogMaxFileCount);
%attribute(kkt_driver::classic_interface, int, LogMaxFileSize, Get_LogMaxFileSize, Set_LogMaxFileSize);
%attribute(kkt_driver::classic_interface, bool, LogOn, Get_LogOn, Set_LogOn);
%attribute(kkt_driver::classic_interface, int, MAXValueOfField, Get_MAXValueOfField);
%attribute(kkt_driver::classic_interface, int, MessageCount, Get_MessageCount, Set_MessageCount);
%attribute(kkt_driver::classic_interface, int, MessageState, Get_MessageState, Set_MessageState);
%attributestring(kkt_driver::classic_interface, std::string, MethodName, Get_MethodName, Set_MethodName);
%attributestring(kkt_driver::classic_interface, std::string, MFPNumber, Get_MFPNumber, Set_MFPNumber);
%attribute(kkt_driver::classic_interface, int, MFPStatus, Get_MFPStatus, Set_MFPStatus);
%attribute(kkt_driver::classic_interface, int, MINValueOfField, Get_MINValueOfField);
%attribute(kkt_driver::classic_interface, bool, MobilePayEnabled, Get_MobilePayEnabled, Set_MobilePayEnabled);
%attribute(kkt_driver::classic_interface, int, ModelID, Get_ModelID, Set_ModelID);
%attribute(kkt_driver::classic_interface, int, ModelIndex, Get_ModelIndex, Set_ModelIndex);
%attributestring(kkt_driver::classic_interface, std::string, ModelNames, Get_ModelNames);
%attribute(kkt_driver::classic_interface, int, ModelParamCount, Get_ModelParamCount);
%attributestring(kkt_driver::classic_interface, std::string, ModelParamDescription, Get_ModelParamDescription);
%attribute(kkt_driver::classic_interface, int, ModelParamIndex, Get_ModelParamIndex, Set_ModelParamIndex);
%attribute(kkt_driver::classic_interface, int, ModelParamNumber, Get_ModelParamNumber, Set_ModelParamNumber);
%attribute(kkt_driver::classic_interface, bool, ModelParamValue, ReadModelParamValue);
%attribute(kkt_driver::classic_interface, int, ModelsCount, Get_ModelsCount);
%attribute(kkt_driver::classic_interface, int, MultiplicationFont, Get_MultiplicationFont, Set_MultiplicationFont);
%attributestring(kkt_driver::classic_interface, std::string, NameCashReg, Get_NameCashReg);
%attributestring(kkt_driver::classic_interface, std::string, NameCashRegEx, Get_NameCashRegEx);
%attributestring(kkt_driver::classic_interface, std::string, NameOperationReg, Get_NameOperationReg);
%attribute(kkt_driver::classic_interface, int, NewPasswordTI, Get_NewPasswordTI, Set_NewPasswordTI);
%attribute(kkt_driver::classic_interface, int, NewSCPassword, Get_NewSCPassword, Set_NewSCPassword);
%attribute(kkt_driver::classic_interface, int, NumberOfCopies, Get_NumberOfCopies, Set_NumberOfCopies);
%attribute(kkt_driver::classic_interface, bool, OFDTicketReceived, Get_OFDTicketReceived, Set_OFDTicketReceived);
%attribute(kkt_driver::classic_interface, int, OPBarcodeInputType, Get_OPBarcodeInputType, Set_OPBarcodeInputType);
%attribute(kkt_driver::classic_interface, int, OpenDocumentNumber, Get_OpenDocumentNumber);
%attribute(kkt_driver::classic_interface, int, OperationBlockFirstString, Get_OperationBlockFirstString, Set_OperationBlockFirstString);
%attribute(kkt_driver::classic_interface, int, OperationNameFont, Get_OperationNameFont, Set_OperationNameFont);
%attribute(kkt_driver::classic_interface, int, OperationNameOffset, Get_OperationNameOffset, Set_OperationNameOffset);
%attribute(kkt_driver::classic_interface, int, OperationNameStringNumber, Get_OperationNameStringNumber, Set_OperationNameStringNumber);
%attribute(kkt_driver::classic_interface, int, OperatorNumber, Get_OperatorNumber);
%attribute(kkt_driver::classic_interface, int, OperationType, Get_OperationType, Set_OperationType);
%attributestring(kkt_driver::classic_interface, std::string, OPIdPayment, Get_OPIdPayment, Set_OPIdPayment);
%attribute(kkt_driver::classic_interface, int, OPRequisiteNumber, Get_OPRequisiteNumber, Set_OPRequisiteNumber);
%attributestring(kkt_driver::classic_interface, std::string, OPRequisiteValue, Get_OPRequisiteValue, Set_OPRequisiteValue);
%attribute(kkt_driver::classic_interface, int, OPSystem, Get_OPSystem, Set_OPSystem);
%attribute(kkt_driver::classic_interface, int, OPTransactionStatus, Get_OPTransactionStatus, Set_OPTransactionStatus);
%attribute(kkt_driver::classic_interface, int, OPTransactionType, Get_OPTransactionType, Set_OPTransactionType);
%attributestring(kkt_driver::classic_interface, std::string, ParameterValue, Get_ParameterValue, Set_ParameterValue);
%attribute(kkt_driver::classic_interface, int, ParentWnd, Get_ParentWnd, Set_ParentWnd);
%attribute(kkt_driver::classic_interface, int, Password, Get_Password, Set_Password);
%attribute(kkt_driver::classic_interface, int, PayDepartment, Get_PayDepartment, Set_PayDepartment);
%attribute(kkt_driver::classic_interface, int, PaymentItemSign, Get_PaymentItemSign, Set_PaymentItemSign);
%attribute(kkt_driver::classic_interface, int, PaymentTypeSign, Get_PaymentTypeSign, Set_PaymentTypeSign);
%attribute(kkt_driver::classic_interface, int, PermitActivizationCode, Get_PermitActivizationCode, Set_PermitActivizationCode);
%attribute(kkt_driver::classic_interface, int, PingResult, Get_PingResult, Set_PingResult);
%attribute(kkt_driver::classic_interface, int, PingTime, Get_PingTime, Set_PingTime);
%attribute(kkt_driver::classic_interface, bool, PointPosition, Get_PointPosition, Set_PointPosition);
%attribute(kkt_driver::classic_interface, int, Poll1, Get_Poll1);
%attribute(kkt_driver::classic_interface, int, Poll2, Get_Poll2);
%attributestring(kkt_driver::classic_interface, std::string, PosControlReceiptSeparator, Get_PosControlReceiptSeparator, Set_PosControlReceiptSeparator);
%attribute(kkt_driver::classic_interface, bool, PortLocked, Get_PortLocked);
%attribute(kkt_driver::classic_interface, int, PortNumber, Get_PortNumber, Set_PortNumber);
%attributestring(kkt_driver::classic_interface, double, PowerSourceVoltage, Get_PowerSourceVoltage);
%attribute(kkt_driver::classic_interface, int, PrepareActivizationRemainCount, Get_PrepareActivizationRemainCount, Set_PrepareActivizationRemainCount);
%attribute(kkt_driver::classic_interface, bool, PresenterIn, Get_PresenterIn);
%attribute(kkt_driver::classic_interface, bool, PresenterOut, Get_PresenterOut);
%attribute(kkt_driver::classic_interface, int64_t, Price, Get_Price, Set_Price);
%attribute(kkt_driver::classic_interface, int, PriceFont, Get_PriceFont, Set_PriceFont);
%attribute(kkt_driver::classic_interface, int, PriceSymbolNumber, Get_PriceSymbolNumber, Set_PriceSymbolNumber);
%attribute(kkt_driver::classic_interface, int, PrintBarcodeText, Get_PrintBarcodeText, Set_PrintBarcodeText);
%attribute(kkt_driver::classic_interface, int, PrintBufferFormat, Get_PrintBufferFormat, Set_PrintBufferFormat);
%attribute(kkt_driver::classic_interface, int, PrintBufferLineNumber, ReadPrintBufferLineNumber);
%attribute(kkt_driver::classic_interface, int, PrintingAlignment, Get_PrintingAlignment, Set_PrintingAlignment);
%attribute(kkt_driver::classic_interface, bool, PrintJournalBeforeZReport, Get_PrintJournalBeforeZReport, Set_PrintJournalBeforeZReport);
%attribute(kkt_driver::classic_interface, int, PrintWidth, Get_PrintWidth);
%attributestring(kkt_driver::classic_interface, std::string, PropertyName, Get_PropertyName, Set_PropertyName);
%attribute(kkt_driver::classic_interface, int, ProtocolType, Get_ProtocolType, Set_ProtocolType);
%attribute(kkt_driver::classic_interface, double, Quantity, Get_Quantity,Set_Quantity);
%attribute(kkt_driver::classic_interface, int, QuantityFont, Get_QuantityFont, Set_QuantityFont);
%attribute(kkt_driver::classic_interface, int, QuantityFormat, Get_QuantityFormat, Set_QuantityFormat);
%attribute(kkt_driver::classic_interface, int, QuantityOffset, Get_QuantityOffset, Set_QuantityOffset);
%attribute(kkt_driver::classic_interface, int, QuantityOfOperations, Get_QuantityOfOperations);
%attribute(kkt_driver::classic_interface, bool, QuantityPointPosition, Get_QuantityPointPosition);
%attribute(kkt_driver::classic_interface, int, QuantityStringNumber, Get_QuantityStringNumber, Set_QuantityStringNumber);
%attribute(kkt_driver::classic_interface, int, QuantitySymbolNumber, Get_QuantitySymbolNumber, Set_QuantitySymbolNumber);
%attribute(kkt_driver::classic_interface, int, RealPayDepartment, Get_RealPayDepartment, Set_RealPayDepartment);
%attribute(kkt_driver::classic_interface, int, ReceiptNumber, Get_ReceiptNumber, Set_ReceiptNumber);
%attribute(kkt_driver::classic_interface, int, ReceiptOutputType, Get_ReceiptOutputType, Set_ReceiptOutputType);
%attribute(kkt_driver::classic_interface, bool, ReceiptRibbonIsPresent, Get_ReceiptRibbonIsPresent);
%attribute(kkt_driver::classic_interface, bool, ReceiptRibbonLever, Get_ReceiptRibbonLever);
%attribute(kkt_driver::classic_interface, bool, ReceiptRibbonOpticalSensor, Get_ReceiptRibbonOpticalSensor);
%attribute(kkt_driver::classic_interface, bool, ReconnectPort, Get_ReconnectPort, Set_ReconnectPort);
%attribute(kkt_driver::classic_interface, int, RecordCount, Get_RecordCount);
%attribute(kkt_driver::classic_interface, int64_t, RegBuyRec, Get_RegBuyRec);
%attribute(kkt_driver::classic_interface, int64_t, RegBuyReturnRec, Get_RegBuyReturnRec);
%attribute(kkt_driver::classic_interface, int64_t, RegBuyReturnSession, Get_RegBuyReturnSession);
%attribute(kkt_driver::classic_interface, int64_t, RegBuySession, Get_RegBuySession);
%attribute(kkt_driver::classic_interface, int, RegisterNumber, Get_RegisterNumber, Set_RegisterNumber);
%attribute(kkt_driver::classic_interface, int, RegistrationNumber, Get_RegistrationNumber, Set_RegistrationNumber);
%attribute(kkt_driver::classic_interface, int, RegistrationReasonCode, Get_RegistrationReasonCode, Set_RegistrationReasonCode);
%attribute(kkt_driver::classic_interface, int64_t, RegSaleRec, Get_RegSaleRec);
%attribute(kkt_driver::classic_interface, int64_t, RegSaleReturnRec, Get_RegSaleReturnRec);
%attribute(kkt_driver::classic_interface, int64_t, RegSaleReturnSession, Get_RegSaleReturnSession);
%attribute(kkt_driver::classic_interface, int64_t, RegSaleSession, Get_RegSaleSession);
%attribute(kkt_driver::classic_interface, bool, ReportType, Get_ReportType, Set_ReportType);
%attribute(kkt_driver::classic_interface, int, ReportTypeInt, Get_ReportTypeInt, Set_ReportTypeInt);
%attribute(kkt_driver::classic_interface, bool, RequestErrorDescription, Get_RequestErrorDescription, Set_RequestErrorDescription);
%attribute(kkt_driver::classic_interface, int, RequestType, Get_RequestType, Set_RequestType);
%attribute(kkt_driver::classic_interface, int, ResultCode, Get_ResultCode);
%attributestring(kkt_driver::classic_interface, std::string, ResultCodeDescription, Get_ResultCodeDescription);
%attributestring(kkt_driver::classic_interface, std::string, RNM, Get_RNM, Set_RNM);
%attribute(kkt_driver::classic_interface, int, RoundingSumm, Get_RoundingSumm, Set_RoundingSumm);
%attribute(kkt_driver::classic_interface, int, RowNumber, Get_RowNumber, Set_RowNumber);
%attribute(kkt_driver::classic_interface, int, RunningPeriod, Get_RunningPeriod, Set_RunningPeriod);
%attribute(kkt_driver::classic_interface, bool, SaleError, Get_SaleError, Set_SaleError);
%attribute(kkt_driver::classic_interface, int, SaveSettingsType, Get_SaveSettingsType, Set_SaveSettingsType);
%attribute(kkt_driver::classic_interface, int, SCPassword, Get_SCPassword, Set_SCPassword);
%attribute(kkt_driver::classic_interface, int, SearchTimeout, Get_SearchTimeout, Set_SearchTimeout);
%attributestring(kkt_driver::classic_interface, std::string, SerialNumber, Get_SerialNumber, Set_SerialNumber);
%attribute(kkt_driver::classic_interface, int, SerialNumberAsInteger, Get_SerialNumberAsInteger);
%attribute(kkt_driver::classic_interface, bool, ServerConnected, Get_ServerConnected);
%attributestring(kkt_driver::classic_interface, std::string, ServerVersion, Get_ServerVersion);
%attribute(kkt_driver::classic_interface, int, SessionNumber, Get_SessionNumber, Set_SessionNumber);
%attribute(kkt_driver::classic_interface, bool, ShowProgress, Get_ShowProgress, Set_ShowProgress);
%attribute(kkt_driver::classic_interface, bool, ShowTagNumber, Get_ShowTagNumber, Set_ShowTagNumber);
%attribute(kkt_driver::classic_interface, int, SKNOError, Get_SKNOError, Set_SKNOError);
%attributestring(kkt_driver::classic_interface, std::string, SKNOIdentifier, Get_SKNOIdentifier, Set_SKNOIdentifier);
%attribute(kkt_driver::classic_interface, int, SKNOStatus, Get_SKNOStatus, Set_SKNOStatus);
%attribute(kkt_driver::classic_interface, bool, SlipDocumentIsMoving, Get_SlipDocumentIsMoving);
%attribute(kkt_driver::classic_interface, bool, SlipDocumentIsPresent, Get_SlipDocumentIsPresent);
%attribute(kkt_driver::classic_interface, int, SlipDocumentLength, Get_SlipDocumentLength, Set_SlipDocumentLength);
%attribute(kkt_driver::classic_interface, int, SlipDocumentWidth, Get_SlipDocumentWidth, Set_SlipDocumentWidth);
%attribute(kkt_driver::classic_interface, int, SlipEqualStringIntervals, Get_SlipEqualStringIntervals, Set_SlipEqualStringIntervals);
%attribute(kkt_driver::classic_interface, int, SlipStringInterval, Get_SlipStringInterval, Set_SlipStringInterval);
%attributestring(kkt_driver::classic_interface, std::string, SlipStringIntervals, Get_SlipStringIntervals, Set_SlipStringIntervals);
%attributestring(kkt_driver::classic_interface, std::string, StringForPrinting, Get_StringForPrinting, Set_StringForPrinting);
%attribute(kkt_driver::classic_interface, int, StringNumber, Get_StringNumber, Set_StringNumber);
%attribute(kkt_driver::classic_interface, int, StringQuantity, Get_StringQuantity, Set_StringQuantity);
%attribute(kkt_driver::classic_interface, int, StringQuantityInOperation, Get_StringQuantityInOperation, Set_StringQuantityInOperation);
%attribute(kkt_driver::classic_interface, int, SubTotalFont, Get_SubTotalFont, Set_SubTotalFont);
%attribute(kkt_driver::classic_interface, int, SubTotalOffset, Get_SubTotalOffset, Set_SubTotalOffset);
%attribute(kkt_driver::classic_interface, int, SubTotalStringNumber, Get_SubTotalStringNumber, Set_SubTotalStringNumber);
%attribute(kkt_driver::classic_interface, int, SubTotalSumFont, Get_SubTotalSumFont, Set_SubTotalSumFont);
%attribute(kkt_driver::classic_interface, int, SubTotalSumOffset, Get_SubTotalSumOffset, Set_SubTotalSumOffset);
%attribute(kkt_driver::classic_interface, int, SubTotalSymbolNumber, Get_SubTotalSymbolNumber, Set_SubTotalSymbolNumber);
%attribute(kkt_driver::classic_interface, int64_t, Summ1, Get_Summ1, Set_Summ1);
%attribute(kkt_driver::classic_interface, int, Summ1Font, Get_Summ1Font, Set_Summ1Font);
%attribute(kkt_driver::classic_interface, int, Summ1NameFont, Get_Summ1NameFont, Set_Summ1NameFont);
%attribute(kkt_driver::classic_interface, int, Summ1NameOffset, Get_Summ1NameOffset, Set_Summ1NameOffset);
%attribute(kkt_driver::classic_interface, int, Summ1Offset, Get_Summ1Offset, Set_Summ1Offset);
%attribute(kkt_driver::classic_interface, int, Summ1StringNumber, Get_Summ1StringNumber, Set_Summ1StringNumber);
%attribute(kkt_driver::classic_interface, int, Summ1SymbolNumber, Get_Summ1SymbolNumber, Set_Summ1SymbolNumber);
%attribute(kkt_driver::classic_interface, int64_t, Summ2, Get_Summ2, Set_Summ2);
%attribute(kkt_driver::classic_interface, int, Summ2Font, Get_Summ2Font, Set_Summ2Font);
%attribute(kkt_driver::classic_interface, int, Summ2NameFont, Get_Summ2NameFont, Set_Summ2NameFont);
%attribute(kkt_driver::classic_interface, int, Summ2NameOffset, Get_Summ2NameOffset, Set_Summ2NameOffset);
%attribute(kkt_driver::classic_interface, int, Summ2Offset, Get_Summ2Offset, Set_Summ2Offset);
%attribute(kkt_driver::classic_interface, int, Summ2StringNumber, Get_Summ2StringNumber, Set_Summ2StringNumber);
%attribute(kkt_driver::classic_interface, int, Summ2SymbolNumber, Get_Summ2SymbolNumber, Set_Summ2SymbolNumber);
%attribute(kkt_driver::classic_interface, int64_t, Summ3, Get_Summ3, Set_Summ3);
%attribute(kkt_driver::classic_interface, int, Summ3Font, Get_Summ3Font, Set_Summ3Font);
%attribute(kkt_driver::classic_interface, int, Summ3NameFont, Get_Summ3NameFont, Set_Summ3NameFont);
%attribute(kkt_driver::classic_interface, int, Summ3NameOffset, Get_Summ3NameOffset, Set_Summ3NameOffset);
%attribute(kkt_driver::classic_interface, int, Summ3Offset, Get_Summ3Offset, Set_Summ3Offset);
%attribute(kkt_driver::classic_interface, int, Summ3StringNumber, Get_Summ3StringNumber, Set_Summ3StringNumber);
%attribute(kkt_driver::classic_interface, int, Summ3SymbolNumber, Get_Summ3SymbolNumber, Set_Summ3SymbolNumber);
%attribute(kkt_driver::classic_interface, int64_t, Summ4, Get_Summ4, Set_Summ4);
%attribute(kkt_driver::classic_interface, int, Summ4Font, Get_Summ4Font, Set_Summ4Font);
%attribute(kkt_driver::classic_interface, int, Summ4NameFont, Get_Summ4NameFont, Set_Summ4NameFont);
%attribute(kkt_driver::classic_interface, int, Summ4NameOffset, Get_Summ4NameOffset, Set_Summ4NameOffset);
%attribute(kkt_driver::classic_interface, int, Summ4Offset, Get_Summ4Offset, Set_Summ4Offset);
%attribute(kkt_driver::classic_interface, int, Summ4StringNumber, Get_Summ4StringNumber, Set_Summ4StringNumber);
%attribute(kkt_driver::classic_interface, int, Summ4SymbolNumber, Get_Summ4SymbolNumber, Set_Summ4SymbolNumber);
%attribute(kkt_driver::classic_interface, int64_t, Summ5, Get_Summ5, Set_Summ5);
%attribute(kkt_driver::classic_interface, int64_t, Summ6, Get_Summ6, Set_Summ6);
%attribute(kkt_driver::classic_interface, int64_t, Summ7, Get_Summ7, Set_Summ7);
%attribute(kkt_driver::classic_interface, int64_t, Summ8, Get_Summ8, Set_Summ8);
%attribute(kkt_driver::classic_interface, int64_t, Summ9, Get_Summ9, Set_Summ9);
%attribute(kkt_driver::classic_interface, int64_t, Summ10, Get_Summ10, Set_Summ10);
%attribute(kkt_driver::classic_interface, int64_t, Summ11, Get_Summ11, Set_Summ11);
%attribute(kkt_driver::classic_interface, int64_t, Summ12, Get_Summ12, Set_Summ12);
%attribute(kkt_driver::classic_interface, int64_t, Summ13, Get_Summ13, Set_Summ13);
%attribute(kkt_driver::classic_interface, int64_t, Summ14, Get_Summ14, Set_Summ14);
%attribute(kkt_driver::classic_interface, int64_t, Summ15, Get_Summ15, Set_Summ15);
%attribute(kkt_driver::classic_interface, int64_t, Summ16, Get_Summ16, Set_Summ16);
%attribute(kkt_driver::classic_interface, int64_t, Summ17, Get_Summ17, Set_Summ17);
%attribute(kkt_driver::classic_interface, int64_t, Summ18, Get_Summ18, Set_Summ18);
%attribute(kkt_driver::classic_interface, int64_t, Summ19, Get_Summ19, Set_Summ19);
%attribute(kkt_driver::classic_interface, int64_t, Summ20, Get_Summ20, Set_Summ20);
%attribute(kkt_driver::classic_interface, int, SummFont, Get_SummFont, Set_SummFont);
%attribute(kkt_driver::classic_interface, int, SummOffset, Get_SummOffset, Set_SummOffset);
%attribute(kkt_driver::classic_interface, int, SummStringNumber, Get_SummStringNumber, Set_SummStringNumber);
%attribute(kkt_driver::classic_interface, int, SummSymbolNumber, Get_SummSymbolNumber, Set_SummSymbolNumber);
%attribute(kkt_driver::classic_interface, int, SwapBytesMode, Get_SwapBytesMode, Set_SwapBytesMode);
%attribute(kkt_driver::classic_interface, int, SyncTimeout, Get_SyncTimeout, Set_SyncTimeout);
%attribute(kkt_driver::classic_interface, int, SysAdminPassword, Get_SysAdminPassword, Set_SysAdminPassword);
%attributestring(kkt_driver::classic_interface, std::string, TableName, Get_TableName);
%attribute(kkt_driver::classic_interface, int, TableNumber, Get_TableNumber, Set_TableNumber);
%attributestring(kkt_driver::classic_interface, std::string, TagDescription, Get_TagDescription, Set_TagDescription);
%attribute(kkt_driver::classic_interface, int, TagID, Get_TagID, Set_TagID);
%attribute(kkt_driver::classic_interface, int, TagType, Get_TagType, Set_TagType);
%attribute(kkt_driver::classic_interface, int, TagNumber, Get_TagNumber, Set_TagNumber);
%attributestring(kkt_driver::classic_interface, std::string, TagValueBin, Get_TagValueBin, Set_TagValueBin);
%attribute(kkt_driver::classic_interface, std::time_t, TagValueDateTime, Get_TagValueDateTime, Set_TagValueDateTime);
%attribute(kkt_driver::classic_interface, int64_t, TagValueFVLN, Get_TagValueFVLN, Set_TagValueFVLN);
%attribute(kkt_driver::classic_interface, int, TagValueLength, Get_TagValueLength, Set_TagValueLength);
%attribute(kkt_driver::classic_interface, int, TagValueInt, Get_TagValueInt, Set_TagValueInt);
%attributestring(kkt_driver::classic_interface, std::string, TagValueStr, Get_TagValueStr, Set_TagValueStr);
%attribute(kkt_driver::classic_interface, int64_t, TaxValue1, Get_TaxValue1, Set_TaxValue1);
%attribute(kkt_driver::classic_interface, int64_t, TaxValue2, Get_TaxValue2, Set_TaxValue2);
%attribute(kkt_driver::classic_interface, int64_t, TaxValue3, Get_TaxValue3, Set_TaxValue3);
%attribute(kkt_driver::classic_interface, int64_t, TaxValue4, Get_TaxValue4, Set_TaxValue4);
%attribute(kkt_driver::classic_interface, int64_t, TaxValue5, Get_TaxValue5, Set_TaxValue5);
%attribute(kkt_driver::classic_interface, int64_t, TaxValue6, Get_TaxValue6, Set_TaxValue6);
%attribute(kkt_driver::classic_interface, int64_t, TaxValue7, Get_TaxValue7, Set_TaxValue7);
%attribute(kkt_driver::classic_interface, int64_t, TaxValue8, Get_TaxValue8, Set_TaxValue8);
%attribute(kkt_driver::classic_interface, int64_t, TaxValue9, Get_TaxValue9, Set_TaxValue9);
%attribute(kkt_driver::classic_interface, int64_t, TaxValue10, Get_TaxValue10, Set_TaxValue10);
%attribute(kkt_driver::classic_interface, int, TaxValue1Enabled, Get_TaxValue1Enabled, Set_TaxValue1Enabled);
%attribute(kkt_driver::classic_interface, int, Tax1, Get_Tax1, Set_Tax1);
%attribute(kkt_driver::classic_interface, int, Tax1NameFont, Get_Tax1NameFont, Set_Tax1NameFont);
%attribute(kkt_driver::classic_interface, int, Tax1NameOffset, Get_Tax1NameOffset, Set_Tax1NameOffset);
%attribute(kkt_driver::classic_interface, int, Tax1NameSymbolNumber, Get_Tax1NameSymbolNumber, Set_Tax1NameSymbolNumber);
%attribute(kkt_driver::classic_interface, int, Tax1RateFont, Get_Tax1RateFont, Set_Tax1RateFont);
%attribute(kkt_driver::classic_interface, int, Tax1RateOffset, Get_Tax1RateOffset, Set_Tax1RateOffset);
%attribute(kkt_driver::classic_interface, int, Tax1RateSymbolNumber, Get_Tax1RateSymbolNumber, Set_Tax1RateSymbolNumber);
%attribute(kkt_driver::classic_interface, int, Tax1SumFont, Get_Tax1SumFont, Set_Tax1SumFont);
%attribute(kkt_driver::classic_interface, int, Tax1SumOffset, Get_Tax1SumOffset, Set_Tax1SumOffset);
%attribute(kkt_driver::classic_interface, int, Tax1SumStringNumber, Get_Tax1SumStringNumber, Set_Tax1SumStringNumber);
%attribute(kkt_driver::classic_interface, int, Tax1SumSymbolNumber, Get_Tax1SumSymbolNumber, Set_Tax1SumSymbolNumber);
%attribute(kkt_driver::classic_interface, int, Tax1TurnOverOffset, Get_Tax1TurnOverOffset, Set_Tax1TurnOverOffset);
%attribute(kkt_driver::classic_interface, int, Tax1TurnOverStringNumber, Get_Tax1TurnOverStringNumber, Set_Tax1TurnOverStringNumber);
%attribute(kkt_driver::classic_interface, int, Tax2, Get_Tax2, Set_Tax2);
%attribute(kkt_driver::classic_interface, int, Tax2NameFont, Get_Tax2NameFont, Set_Tax2NameFont);
%attribute(kkt_driver::classic_interface, int, Tax2NameOffset, Get_Tax2NameOffset, Set_Tax2NameOffset);
%attribute(kkt_driver::classic_interface, int, Tax2NameSymbolNumber, Get_Tax2NameSymbolNumber, Set_Tax2NameSymbolNumber);
%attribute(kkt_driver::classic_interface, int, Tax2RateFont, Get_Tax2RateFont, Set_Tax2RateFont);
%attribute(kkt_driver::classic_interface, int, Tax2RateOffset, Get_Tax2RateOffset, Set_Tax2RateOffset);
%attribute(kkt_driver::classic_interface, int, Tax2RateSymbolNumber, Get_Tax2RateSymbolNumber, Set_Tax2RateSymbolNumber);
%attribute(kkt_driver::classic_interface, int, Tax2SumFont, Get_Tax2SumFont, Set_Tax2SumFont);
%attribute(kkt_driver::classic_interface, int, Tax2SumOffset, Get_Tax2SumOffset, Set_Tax2SumOffset);
%attribute(kkt_driver::classic_interface, int, Tax2SumStringNumber, Get_Tax2SumStringNumber, Set_Tax2SumStringNumber);
%attribute(kkt_driver::classic_interface, int, Tax2SumSymbolNumber, Get_Tax2SumSymbolNumber, Set_Tax2SumSymbolNumber);
%attribute(kkt_driver::classic_interface, int, Tax2TurnOverOffset, Get_Tax2TurnOverOffset, Set_Tax2TurnOverOffset);
%attribute(kkt_driver::classic_interface, int, Tax2TurnOverOffset, Get_Tax2TurnOverOffset, Set_Tax2TurnOverOffset);
%attribute(kkt_driver::classic_interface, int, Tax2TurnOverStringNumber, Get_Tax2TurnOverStringNumber, Set_Tax2TurnOverStringNumber);
%attribute(kkt_driver::classic_interface, int, Tax2TurnOverSymbolNumber, Get_Tax2TurnOverSymbolNumber, Set_Tax2TurnOverSymbolNumber);
%attribute(kkt_driver::classic_interface, int, Tax3, Get_Tax3, Set_Tax3);
%attribute(kkt_driver::classic_interface, int, Tax3NameFont, Get_Tax3NameFont, Set_Tax3NameFont);
%attribute(kkt_driver::classic_interface, int, Tax3NameOffset, Get_Tax3NameOffset, Set_Tax3NameOffset);
%attribute(kkt_driver::classic_interface, int, Tax3NameSymbolNumber, Get_Tax3NameSymbolNumber, Set_Tax3NameSymbolNumber);
%attribute(kkt_driver::classic_interface, int, Tax3RateFont, Get_Tax3RateFont, Set_Tax3RateFont);
%attribute(kkt_driver::classic_interface, int, Tax3RateOffset, Get_Tax3RateOffset, Set_Tax3RateOffset);
%attribute(kkt_driver::classic_interface, int, Tax3RateSymbolNumber, Get_Tax3RateSymbolNumber, Set_Tax3RateSymbolNumber);
%attribute(kkt_driver::classic_interface, int, Tax3SumFont, Get_Tax3SumFont, Set_Tax3SumFont);
%attribute(kkt_driver::classic_interface, int, Tax3SumOffset, Get_Tax3SumOffset, Set_Tax3SumOffset);
%attribute(kkt_driver::classic_interface, int, Tax3SumStringNumber, Get_Tax3SumStringNumber, Set_Tax3SumStringNumber);
%attribute(kkt_driver::classic_interface, int, Tax3SumSymbolNumber, Get_Tax3SumSymbolNumber, Set_Tax3SumSymbolNumber);
%attribute(kkt_driver::classic_interface, int, Tax3TurnOverOffset, Get_Tax3TurnOverOffset, Set_Tax3TurnOverOffset);
%attribute(kkt_driver::classic_interface, int, Tax3TurnOverOffset, Get_Tax3TurnOverOffset, Set_Tax3TurnOverOffset);
%attribute(kkt_driver::classic_interface, int, Tax3TurnOverStringNumber, Get_Tax3TurnOverStringNumber, Set_Tax3TurnOverStringNumber);
%attribute(kkt_driver::classic_interface, int, Tax3TurnOverSymbolNumber, Get_Tax3TurnOverSymbolNumber, Set_Tax3TurnOverSymbolNumber);
%attribute(kkt_driver::classic_interface, int, Tax4, Get_Tax4, Set_Tax4);
%attribute(kkt_driver::classic_interface, int, Tax4NameFont, Get_Tax4NameFont, Set_Tax4NameFont);
%attribute(kkt_driver::classic_interface, int, Tax4NameOffset, Get_Tax4NameOffset, Set_Tax4NameOffset);
%attribute(kkt_driver::classic_interface, int, Tax4NameSymbolNumber, Get_Tax4NameSymbolNumber, Set_Tax4NameSymbolNumber);
%attribute(kkt_driver::classic_interface, int, Tax4RateFont, Get_Tax4RateFont, Set_Tax4RateFont);
%attribute(kkt_driver::classic_interface, int, Tax4RateOffset, Get_Tax4RateOffset, Set_Tax4RateOffset);
%attribute(kkt_driver::classic_interface, int, Tax4RateSymbolNumber, Get_Tax4RateSymbolNumber, Set_Tax4RateSymbolNumber);
%attribute(kkt_driver::classic_interface, int, Tax4SumFont, Get_Tax4SumFont, Set_Tax4SumFont);
%attribute(kkt_driver::classic_interface, int, Tax4SumOffset, Get_Tax4SumOffset, Set_Tax4SumOffset);
%attribute(kkt_driver::classic_interface, int, Tax4SumStringNumber, Get_Tax4SumStringNumber, Set_Tax4SumStringNumber);
%attribute(kkt_driver::classic_interface, int, Tax4SumSymbolNumber, Get_Tax4SumSymbolNumber, Set_Tax4SumSymbolNumber);
%attribute(kkt_driver::classic_interface, int, Tax4TurnOverOffset, Get_Tax4TurnOverOffset, Set_Tax4TurnOverOffset);
%attribute(kkt_driver::classic_interface, int, Tax4TurnOverOffset, Get_Tax4TurnOverOffset, Set_Tax4TurnOverOffset);
%attribute(kkt_driver::classic_interface, int, Tax4TurnOverStringNumber, Get_Tax4TurnOverStringNumber, Set_Tax4TurnOverStringNumber);
%attribute(kkt_driver::classic_interface, int, Tax4TurnOverSymbolNumber, Get_Tax4TurnOverSymbolNumber, Set_Tax4TurnOverSymbolNumber);
%attribute(kkt_driver::classic_interface, int, TaxType, Get_TaxType, Set_TaxType);
%attribute(kkt_driver::classic_interface, int, TCPConnectionTimeout, Get_TCPConnectionTimeout, Set_TCPConnectionTimeout);
%attribute(kkt_driver::classic_interface, int, TCPPort, Get_TCPPort, Set_TCPPort);
%attributestring(kkt_driver::classic_interface, std::string, TextBlock, Get_TextBlock, Set_TextBlock);
%attribute(kkt_driver::classic_interface, int, TextBlockNumber, Get_TextBlockNumber, Set_TextBlockNumber);
%attribute(kkt_driver::classic_interface, int, TextFont, Get_TextFont, Set_TextFont);
%attribute(kkt_driver::classic_interface, int, TextOffset, Get_TextOffset, Set_TextOffset);
%attribute(kkt_driver::classic_interface, int, TextStringNumber, Get_TextStringNumber, Set_TextStringNumber);
%attribute(kkt_driver::classic_interface, int, TextSymbolNumber, Get_TextSymbolNumber, Set_TextSymbolNumber);
%attribute(kkt_driver::classic_interface, std::time_t, Time, Get_Time, Set_Time);
%attribute(kkt_driver::classic_interface, std::time_t, Time2, Get_Time2, Set_Time2);
%attribute(kkt_driver::classic_interface, int, Timeout, Get_Timeout, Set_Timeout);
%attribute(kkt_driver::classic_interface, int, TimeoutsUsing, Get_TimeoutsUsing, Set_TimeoutsUsing);
%attributestring(kkt_driver::classic_interface, std::string, TimeStr, Get_TimeStr, Set_TimeStr);
%attributeval(kkt_driver::classic_interface, std::vector<uint8_t>, TLVData, Get_TLVData, Set_TLVData);
%attributestring(kkt_driver::classic_interface, std::string, TLVDataHex, Get_TLVDataHex, Set_TLVDataHex);
%attributestring(kkt_driver::classic_interface, std::string, Token, Get_Token, Set_Token);
%attribute(kkt_driver::classic_interface, int, TotalFont, Get_TotalFont, Set_TotalFont);
%attribute(kkt_driver::classic_interface, int, TotalOffset, Get_TotalOffset, Set_TotalOffset);
%attribute(kkt_driver::classic_interface, int, TotalStringNumber, Get_TotalStringNumber, Set_TotalStringNumber);
%attribute(kkt_driver::classic_interface, int, TotalSumFont, Get_TotalSumFont, Set_TotalSumFont);
%attribute(kkt_driver::classic_interface, int, TotalSumOffset, Get_TotalSumOffset, Set_TotalSumOffset);
%attribute(kkt_driver::classic_interface, int, TotalSymbolNumber, Get_TotalSymbolNumber, Set_TotalSymbolNumber);
%attributestring(kkt_driver::classic_interface, std::string, TransferBytes, Get_TransferBytes, Set_TransferBytes);
%attribute(kkt_driver::classic_interface, bool, TranslationEnabled, Get_TranslationEnabled, Set_TranslationEnabled);
%attribute(kkt_driver::classic_interface, int, TransmitDocumentNumber, Get_TransmitDocumentNumber);
%attribute(kkt_driver::classic_interface, int, TransmitQueueSize, Get_TransmitQueueSize);
%attribute(kkt_driver::classic_interface, int, TransmitSessionNumber, Get_TransmitSessionNumber);
%attribute(kkt_driver::classic_interface, int, TransmitStatus, Get_TransmitStatus);
%attribute(kkt_driver::classic_interface, bool, TypeOfLastEntryFM, Get_TypeOfLastEntryFM);
%attribute(kkt_driver::classic_interface, int, TypeOfLastEntryFMEx, Get_TypeOfLastEntryFMEx);
%attribute(kkt_driver::classic_interface, bool, TypeOfSumOfEntriesFM, Get_TypeOfSumOfEntriesFM, Set_TypeOfSumOfEntriesFM);
%attribute(kkt_driver::classic_interface, int, UCodePage, Get_UCodePage);
%attributestring(kkt_driver::classic_interface, std::string, UCodePageText, Get_UCodePageText);
%attributestring(kkt_driver::classic_interface, std::string, UDescription, Get_UDescription);
%attribute(kkt_driver::classic_interface, int, UMajorProtocolVersion, Get_UMajorProtocolVersion);
%attribute(kkt_driver::classic_interface, int, UMajorType, Get_UMajorType);
%attribute(kkt_driver::classic_interface, int, UMinorProtocolVersion, Get_UMinorProtocolVersion);
%attribute(kkt_driver::classic_interface, int, UMinorType, Get_UMinorType);
%attribute(kkt_driver::classic_interface, int, UModel, Get_UModel);
%attributestring(kkt_driver::classic_interface, std::string, URL, Get_URL, Set_URL);
%attribute(kkt_driver::classic_interface, bool, UseCommandTimeout, Get_UseCommandTimeout, Set_UseCommandTimeout);
%attribute(kkt_driver::classic_interface, bool, UseIPAddress, Get_UseIPAddress, Set_UseIPAddress);
%attribute(kkt_driver::classic_interface, bool, UseJournalRibbon, Get_UseJournalRibbon, Set_UseJournalRibbon);
%attribute(kkt_driver::classic_interface, bool, UseReceiptRibbon, Get_UseReceiptRibbon, Set_UseReceiptRibbon);
%attribute(kkt_driver::classic_interface, bool, UseSlipCheck, Get_UseSlipCheck, Set_UseSlipCheck);
%attribute(kkt_driver::classic_interface, bool, UseSlipDocument, Get_UseSlipDocument, Set_UseSlipDocument);
%attribute(kkt_driver::classic_interface, bool, UseTaxDiscountBel, Get_UseTaxDiscountBel, Set_UseTaxDiscountBel);
%attribute(kkt_driver::classic_interface, bool, UseWareCode, Get_UseWareCode, Set_UseWareCode);
%attribute(kkt_driver::classic_interface, int, ValueOfFieldInteger, Get_ValueOfFieldInteger, Set_ValueOfFieldInteger);
%attributestring(kkt_driver::classic_interface, std::string, ValueOfFieldString, Get_ValueOfFieldString, Set_ValueOfFieldString);
%attribute(kkt_driver::classic_interface, int, VertScale, Get_VertScale, Set_VertScale);
%attribute(kkt_driver::classic_interface, int, WaitForPrintingDelay, Get_WaitForPrintingDelay, Set_WaitForPrintingDelay);
%attribute(kkt_driver::classic_interface, int, WareCode, Get_WareCode, Set_WareCode);
%attribute(kkt_driver::classic_interface, bool, SkipPrint, Get_SkipPrint, Set_SkipPrint);
%attributestring(kkt_driver::classic_interface, std::string, DigitalSign, Get_DigitalSign, Set_DigitalSign);
%attribute(kkt_driver::classic_interface, int, DeviceFunctionNumber, Get_DeviceFunctionNumber, Set_DeviceFunctionNumber);
%attribute(kkt_driver::classic_interface, int, ValueOfFunctionInteger, Get_ValueOfFunctionInteger, Set_ValueOfFunctionInteger);
%attributestring(kkt_driver::classic_interface, std::string, ValueOfFunctionString, Get_ValueOfFunctionString, Set_ValueOfFunctionString);
%attribute(kkt_driver::classic_interface, bool, EnableCashcoreMarkCompatibility, Get_EnableCashcoreMarkCompatibility, Set_EnableCashcoreMarkCompatibility);
%attribute(kkt_driver::classic_interface, int, MarkingType, Get_MarkingType, Set_MarkingType);
%attribute(kkt_driver::classic_interface, int, MarkingTypeEx, Get_MarkingTypeEx, Set_MarkingTypeEx);
%attribute(kkt_driver::classic_interface, int, DataBlockSize, Get_DataBlockSize, Set_DataBlockSize);
%attribute(kkt_driver::classic_interface, int64_t, MessageNumber, Get_MessageNumber, Set_MessageNumber);
%attribute(kkt_driver::classic_interface, int, CheckItemLocalError, Get_CheckItemLocalError, Set_CheckItemLocalError);
%attribute(kkt_driver::classic_interface, int, MeasureUnit, Get_MeasureUnit, Set_MeasureUnit);
%attribute(kkt_driver::classic_interface, bool, DivisionalQuantity, Get_DivisionalQuantity, Set_DivisionalQuantity);
%attribute(kkt_driver::classic_interface, uint64_t, Numerator, Get_Numerator, Set_Numerator);
%attribute(kkt_driver::classic_interface, uint64_t, Denominator, Get_Denominator, Set_Denominator);
%attribute(kkt_driver::classic_interface, int, FreeMemorySize, Get_FreeMemorySize, Set_FreeMemorySize);
%attribute(kkt_driver::classic_interface, int, MCCheckStatus, Get_MCCheckStatus, Set_MCCheckStatus);
%attribute(kkt_driver::classic_interface, int, MCNotificationStatus, Get_MCNotificationStatus, Set_MCNotificationStatus);
%attribute(kkt_driver::classic_interface, int, MCCommandFlags, Get_MCCommandFlags, Set_MCCommandFlags);
%attribute(kkt_driver::classic_interface, int, MCCheckResultSavedCount, Get_MCCheckResultSavedCount, Set_MCCheckResultSavedCount);
%attribute(kkt_driver::classic_interface, int, MCRealizationCount, Get_MCRealizationCount, Set_MCRealizationCount);
%attribute(kkt_driver::classic_interface, int, MCStorageSize, Get_MCStorageSize, Set_MCStorageSize);
%attribute(kkt_driver::classic_interface, uint64_t, CheckSum, Get_CheckSum, Set_CheckSum);
%attribute(kkt_driver::classic_interface, int, NotificationCount, Get_NotificationCount, Set_NotificationCount);
%attribute(kkt_driver::classic_interface, int64_t, NotificationNumber, Get_NotificationNumber, Set_NotificationNumber);
%attribute(kkt_driver::classic_interface, int, NotificationSize, Get_NotificationSize, Set_NotificationSize);
%attribute(kkt_driver::classic_interface, int, DataOffset, Get_DataOffset, Set_DataOffset);
%attribute(kkt_driver::classic_interface, int, MarkingType2, Get_MarkingType2, Set_MarkingType2);
%attributeval(kkt_driver::classic_interface, std::vector<uint8_t>, RandomSequence, Get_RandomSequence, Set_RandomSequence);
%attributestring(kkt_driver::classic_interface, std::string, RandomSequenceHex, Get_RandomSequenceHex, Set_RandomSequenceHex);
%attributeval(kkt_driver::classic_interface, std::vector<uint8_t>, AuthData, Get_AuthData, Set_AuthData);
%attribute(kkt_driver::classic_interface, int, ItemStatus, Get_ItemStatus, Set_ItemStatus);
%attribute(kkt_driver::classic_interface, int, CheckItemMode, Get_CheckItemMode, Set_CheckItemMode);
%attribute(kkt_driver::classic_interface, int, CheckItemLocalResult, Get_CheckItemLocalResult, Set_CheckItemLocalResult);
%attribute(kkt_driver::classic_interface, int, KMServerErrorCode, Get_KMServerErrorCode, Set_KMServerErrorCode);
%attribute(kkt_driver::classic_interface, int, KMServerCheckingStatus, Get_KMServerCheckingStatus, Set_KMServerCheckingStatus);
%attributestring(kkt_driver::classic_interface, std::string, LoaderVersion, Get_LoaderVersion);
%attribute(kkt_driver::classic_interface, int, LastDocumentNumber, Get_LastDocumentNumber, Set_LastDocumentNumber);
%attribute(kkt_driver::classic_interface, int, FirstDocumentNumber, Get_FirstDocumentNumber, Set_FirstDocumentNumber);
%attribute(kkt_driver::classic_interface, int, FNArchiveType, Get_FNArchiveType, Set_FNArchiveType);
%attribute(kkt_driver::classic_interface, bool, MarkingOnly, Get_MarkingOnly, Set_MarkingOnly);
%attribute(kkt_driver::classic_interface, uint32_t, FN30DayResource, Get_FN30DayResource, Set_FN30DayResource);
%attribute(kkt_driver::classic_interface, uint32_t, FN5YearResource, Get_FN5YearResource, Set_FN5YearResource);
%attributestring(kkt_driver::classic_interface, std::string, CrptExchangeCaCertPath, Get_CrptExchangeCaCertPath, Set_CrptExchangeCaCertPath);
%attributestring(kkt_driver::classic_interface, std::string, CrptCdnListUrl, Get_CrptCdnListUrl, Set_CrptCdnListUrl);
%attributestring(kkt_driver::classic_interface, std::string, CrptToken, Get_CrptToken, Set_CrptToken);
%attributestring(kkt_driver::classic_interface, std::string, OutputStrJson, Get_OutputStrJson, Set_OutputStrJson);
%attributestring(kkt_driver::classic_interface, std::string, InputStrJson, Get_InputStrJson, Set_InputStrJson);
%attribute(kkt_driver::classic_interface, bool, CrptCheck, Get_CrptCheck, Set_CrptCheck);
%attribute(kkt_driver::classic_interface, bool, WrapStrings, Get_WrapStrings, Set_WrapStrings);
%attribute(kkt_driver::classic_interface, int, FNOSUSupportStatus, Get_FNOSUSupportStatus, Set_FNOSUSupportStatus);
%attributestring(kkt_driver::classic_interface, std::string, FNImplementation, Get_FNImplementation, Set_FNImplementation);
%attribute(kkt_driver::classic_interface, int, DocumentSize, Get_DocumentSize, Set_DocumentSize);
%attribute(kkt_driver::classic_interface, bool, AutoOpenSession, Get_AutoOpenSession, Set_AutoOpenSession);
%attribute(kkt_driver::classic_interface, bool, MCOSUSign, Get_MCOSUSign, Set_MCOSUSign);
%attributestring(kkt_driver::classic_interface, std::string, FontHashHex, Get_FontHashHex);
%attributestring(kkt_driver::classic_interface, std::string, DataBlockHex, Get_DataBlockHex);
%attributestring(kkt_driver::classic_interface, std::string, DeclarativeEndpointPath, Get_DeclarativeEndpointPath, Set_DeclarativeEndpointPath);
%attributestring(kkt_driver::classic_interface, std::string, DeclarativeOutput, Get_DeclarativeOutput, Set_DeclarativeOutput);
%attributestring(kkt_driver::classic_interface, std::string, DeclarativeInput, Get_DeclarativeInput, Set_DeclarativeInput);
%attribute(kkt_driver::classic_interface, int64_t, WaitForPrintingTimeout, Get_WaitForPrintingTimeout, Set_WaitForPrintingTimeout);
%attributestring(kkt_driver::classic_interface, std::string, UserAttributeValue, Get_UserAttributeValue, Set_UserAttributeValue);
%attributestring(kkt_driver::classic_interface, std::string, UserAttributeName, Get_UserAttributeName, Set_UserAttributeName);

#endif //SWIGPYTHON

%include <classic_api.h>
