# DumpApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dumpDocumentConfigGET**](DumpApi.md#dumpDocumentConfigGET) | **GET** /api/v1/dump/document-config/ | 
[**dumpDocumentConfigPUT**](DumpApi.md#dumpDocumentConfigPUT) | **PUT** /api/v1/dump/document-config/ | 
[**dumpDumpFixturePOST**](DumpApi.md#dumpDumpFixturePOST) | **POST** /api/v1/dump/dump-fixture/ | 
[**dumpDumpGET**](DumpApi.md#dumpDumpGET) | **GET** /api/v1/dump/dump/ | 
[**dumpDumpPUT**](DumpApi.md#dumpDumpPUT) | **PUT** /api/v1/dump/dump/ | 
[**dumpFieldValuesGET**](DumpApi.md#dumpFieldValuesGET) | **GET** /api/v1/dump/field-values/ | 
[**dumpFieldValuesPUT**](DumpApi.md#dumpFieldValuesPUT) | **PUT** /api/v1/dump/field-values/ | 
[**dumpLoadFixturePOST**](DumpApi.md#dumpLoadFixturePOST) | **POST** /api/v1/dump/load-fixture/ | 


<a name="dumpDocumentConfigGET"></a>
# **dumpDocumentConfigGET**
> Map&lt;String, Object&gt; dumpDocumentConfigGET()



Dump document types, fields, field detectors and  document filters to json.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DumpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: AuthToken
    ApiKeyAuth AuthToken = (ApiKeyAuth) defaultClient.getAuthentication("AuthToken");
    AuthToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AuthToken.setApiKeyPrefix("Token");

    DumpApi apiInstance = new DumpApi(defaultClient);
    try {
      Map<String, Object> result = apiInstance.dumpDocumentConfigGET();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DumpApi#dumpDocumentConfigGET");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Map&lt;String, Object&gt;**

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |

<a name="dumpDocumentConfigPUT"></a>
# **dumpDocumentConfigPUT**
> File dumpDocumentConfigPUT(requestBody)



Upload field values

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DumpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: AuthToken
    ApiKeyAuth AuthToken = (ApiKeyAuth) defaultClient.getAuthentication("AuthToken");
    AuthToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AuthToken.setApiKeyPrefix("Token");

    DumpApi apiInstance = new DumpApi(defaultClient);
    Map<String, Object> requestBody = null; // Map<String, Object> | 
    try {
      File result = apiInstance.dumpDocumentConfigPUT(requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DumpApi#dumpDocumentConfigPUT");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requestBody** | [**Map&lt;String, Object&gt;**](Object.md)|  | [optional]

### Return type

[**File**](File.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

<a name="dumpDumpFixturePOST"></a>
# **dumpDumpFixturePOST**
> File dumpDumpFixturePOST(dumpFixture)



Download model fixture

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DumpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: AuthToken
    ApiKeyAuth AuthToken = (ApiKeyAuth) defaultClient.getAuthentication("AuthToken");
    AuthToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AuthToken.setApiKeyPrefix("Token");

    DumpApi apiInstance = new DumpApi(defaultClient);
    DumpFixture dumpFixture = new DumpFixture(); // DumpFixture | 
    try {
      File result = apiInstance.dumpDumpFixturePOST(dumpFixture);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DumpApi#dumpDumpFixturePOST");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dumpFixture** | [**DumpFixture**](DumpFixture.md)|  | [optional]

### Return type

[**File**](File.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

<a name="dumpDumpGET"></a>
# **dumpDumpGET**
> Map&lt;String, Object&gt; dumpDumpGET()



Dump all users, roles, email addresses, review statuses, review status groups, app vars, document types, fields, field detectors and document filters to json.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DumpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: AuthToken
    ApiKeyAuth AuthToken = (ApiKeyAuth) defaultClient.getAuthentication("AuthToken");
    AuthToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AuthToken.setApiKeyPrefix("Token");

    DumpApi apiInstance = new DumpApi(defaultClient);
    try {
      Map<String, Object> result = apiInstance.dumpDumpGET();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DumpApi#dumpDumpGET");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Map&lt;String, Object&gt;**

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |

<a name="dumpDumpPUT"></a>
# **dumpDumpPUT**
> File dumpDumpPUT(requestBody)



Upload field values

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DumpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: AuthToken
    ApiKeyAuth AuthToken = (ApiKeyAuth) defaultClient.getAuthentication("AuthToken");
    AuthToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AuthToken.setApiKeyPrefix("Token");

    DumpApi apiInstance = new DumpApi(defaultClient);
    Map<String, Object> requestBody = null; // Map<String, Object> | 
    try {
      File result = apiInstance.dumpDumpPUT(requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DumpApi#dumpDumpPUT");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requestBody** | [**Map&lt;String, Object&gt;**](Object.md)|  | [optional]

### Return type

[**File**](File.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

<a name="dumpFieldValuesGET"></a>
# **dumpFieldValuesGET**
> Map&lt;String, Object&gt; dumpFieldValuesGET()



Download field values

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DumpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: AuthToken
    ApiKeyAuth AuthToken = (ApiKeyAuth) defaultClient.getAuthentication("AuthToken");
    AuthToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AuthToken.setApiKeyPrefix("Token");

    DumpApi apiInstance = new DumpApi(defaultClient);
    try {
      Map<String, Object> result = apiInstance.dumpFieldValuesGET();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DumpApi#dumpFieldValuesGET");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Map&lt;String, Object&gt;**

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |

<a name="dumpFieldValuesPUT"></a>
# **dumpFieldValuesPUT**
> File dumpFieldValuesPUT(requestBody)



Upload field values

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DumpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: AuthToken
    ApiKeyAuth AuthToken = (ApiKeyAuth) defaultClient.getAuthentication("AuthToken");
    AuthToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AuthToken.setApiKeyPrefix("Token");

    DumpApi apiInstance = new DumpApi(defaultClient);
    Map<String, Object> requestBody = null; // Map<String, Object> | 
    try {
      File result = apiInstance.dumpFieldValuesPUT(requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DumpApi#dumpFieldValuesPUT");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requestBody** | [**Map&lt;String, Object&gt;**](Object.md)|  | [optional]

### Return type

[**File**](File.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

<a name="dumpLoadFixturePOST"></a>
# **dumpLoadFixturePOST**
> Map&lt;String, Object&gt; dumpLoadFixturePOST(loadFixture)



Install model fixtures

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DumpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: AuthToken
    ApiKeyAuth AuthToken = (ApiKeyAuth) defaultClient.getAuthentication("AuthToken");
    AuthToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AuthToken.setApiKeyPrefix("Token");

    DumpApi apiInstance = new DumpApi(defaultClient);
    LoadFixture loadFixture = new LoadFixture(); // LoadFixture | 
    try {
      Map<String, Object> result = apiInstance.dumpLoadFixturePOST(loadFixture);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DumpApi#dumpLoadFixturePOST");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loadFixture** | [**LoadFixture**](LoadFixture.md)|  | [optional]

### Return type

**Map&lt;String, Object&gt;**

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |

