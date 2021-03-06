# SimilarityApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**similarityPartySimilarityGET**](SimilarityApi.md#similarityPartySimilarityGET) | **GET** /api/v1/similarity/party-similarity/ | 
[**similarityPartySimilarityPOST**](SimilarityApi.md#similarityPartySimilarityPOST) | **POST** /api/v1/similarity/party-similarity/ | 
[**similaritySimilarityByFeaturesGET**](SimilarityApi.md#similaritySimilarityByFeaturesGET) | **GET** /api/v1/similarity/similarity-by-features/ | 
[**similaritySimilarityByFeaturesPOST**](SimilarityApi.md#similaritySimilarityByFeaturesPOST) | **POST** /api/v1/similarity/similarity-by-features/ | 
[**similaritySimilarityGET**](SimilarityApi.md#similaritySimilarityGET) | **GET** /api/v1/similarity/similarity/ | 
[**similaritySimilarityPOST**](SimilarityApi.md#similaritySimilarityPOST) | **POST** /api/v1/similarity/similarity/ | 


<a name="similarityPartySimilarityGET"></a>
# **similarityPartySimilarityGET**
> Map&lt;String, Object&gt; similarityPartySimilarityGET()



\&quot;Party Similarity\&quot; admin task  POST params:     - case_sensitive: bool     - similarity_type: str[]     - similarity_threshold: int     - delete: bool

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SimilarityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: AuthToken
    ApiKeyAuth AuthToken = (ApiKeyAuth) defaultClient.getAuthentication("AuthToken");
    AuthToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AuthToken.setApiKeyPrefix("Token");

    SimilarityApi apiInstance = new SimilarityApi(defaultClient);
    try {
      Map<String, Object> result = apiInstance.similarityPartySimilarityGET();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SimilarityApi#similarityPartySimilarityGET");
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

<a name="similarityPartySimilarityPOST"></a>
# **similarityPartySimilarityPOST**
> SimilarityPOSTObjectResponse similarityPartySimilarityPOST(requestBody)



\&quot;Party Similarity\&quot; admin task  POST params:     - case_sensitive: bool     - similarity_type: str[]     - similarity_threshold: int     - delete: bool

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SimilarityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: AuthToken
    ApiKeyAuth AuthToken = (ApiKeyAuth) defaultClient.getAuthentication("AuthToken");
    AuthToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AuthToken.setApiKeyPrefix("Token");

    SimilarityApi apiInstance = new SimilarityApi(defaultClient);
    Map<String, Object> requestBody = null; // Map<String, Object> | 
    try {
      SimilarityPOSTObjectResponse result = apiInstance.similarityPartySimilarityPOST(requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SimilarityApi#similarityPartySimilarityPOST");
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

[**SimilarityPOSTObjectResponse**](SimilarityPOSTObjectResponse.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

<a name="similaritySimilarityByFeaturesGET"></a>
# **similaritySimilarityByFeaturesGET**
> Map&lt;String, Object&gt; similaritySimilarityByFeaturesGET()



\&quot;Similarity\&quot; admin task  POST params:     - search_similar_documents: bool     - search_similar_text_units: bool     - similarity_threshold: int     - use_idf: bool     - delete: bool     - project: int     - feature_source: list - list[date, definition, duration, court,       currency_name, currency_value, term, party, geoentity]     - unit_type: str sentence|paragraph     - distance_type: str - see scipy.spatial.distance._METRICS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SimilarityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: AuthToken
    ApiKeyAuth AuthToken = (ApiKeyAuth) defaultClient.getAuthentication("AuthToken");
    AuthToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AuthToken.setApiKeyPrefix("Token");

    SimilarityApi apiInstance = new SimilarityApi(defaultClient);
    try {
      Map<String, Object> result = apiInstance.similaritySimilarityByFeaturesGET();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SimilarityApi#similaritySimilarityByFeaturesGET");
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

<a name="similaritySimilarityByFeaturesPOST"></a>
# **similaritySimilarityByFeaturesPOST**
> SimilarityPOSTObjectResponse similaritySimilarityByFeaturesPOST(requestBody)



\&quot;Similarity\&quot; admin task  POST params:     - search_similar_documents: bool     - search_similar_text_units: bool     - similarity_threshold: int     - use_idf: bool     - delete: bool     - project: int     - feature_source: list - list[date, definition, duration, court,       currency_name, currency_value, term, party, geoentity]     - unit_type: str sentence|paragraph     - distance_type: str - see scipy.spatial.distance._METRICS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SimilarityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: AuthToken
    ApiKeyAuth AuthToken = (ApiKeyAuth) defaultClient.getAuthentication("AuthToken");
    AuthToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AuthToken.setApiKeyPrefix("Token");

    SimilarityApi apiInstance = new SimilarityApi(defaultClient);
    Map<String, Object> requestBody = null; // Map<String, Object> | 
    try {
      SimilarityPOSTObjectResponse result = apiInstance.similaritySimilarityByFeaturesPOST(requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SimilarityApi#similaritySimilarityByFeaturesPOST");
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

[**SimilarityPOSTObjectResponse**](SimilarityPOSTObjectResponse.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

<a name="similaritySimilarityGET"></a>
# **similaritySimilarityGET**
> Map&lt;String, Object&gt; similaritySimilarityGET()



\&quot;Similarity\&quot; admin task  POST params:     - search_similar_documents: bool     - search_similar_text_units: bool     - similarity_threshold: int     - use_idf: bool     - delete: bool     - project: bool

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SimilarityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: AuthToken
    ApiKeyAuth AuthToken = (ApiKeyAuth) defaultClient.getAuthentication("AuthToken");
    AuthToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AuthToken.setApiKeyPrefix("Token");

    SimilarityApi apiInstance = new SimilarityApi(defaultClient);
    try {
      Map<String, Object> result = apiInstance.similaritySimilarityGET();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SimilarityApi#similaritySimilarityGET");
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

<a name="similaritySimilarityPOST"></a>
# **similaritySimilarityPOST**
> SimilarityPOSTObjectResponse similaritySimilarityPOST(requestBody)



\&quot;Similarity\&quot; admin task  POST params:     - search_similar_documents: bool     - search_similar_text_units: bool     - similarity_threshold: int     - use_idf: bool     - delete: bool     - project: bool

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SimilarityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: AuthToken
    ApiKeyAuth AuthToken = (ApiKeyAuth) defaultClient.getAuthentication("AuthToken");
    AuthToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AuthToken.setApiKeyPrefix("Token");

    SimilarityApi apiInstance = new SimilarityApi(defaultClient);
    Map<String, Object> requestBody = null; // Map<String, Object> | 
    try {
      SimilarityPOSTObjectResponse result = apiInstance.similaritySimilarityPOST(requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SimilarityApi#similaritySimilarityPOST");
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

[**SimilarityPOSTObjectResponse**](SimilarityPOSTObjectResponse.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

