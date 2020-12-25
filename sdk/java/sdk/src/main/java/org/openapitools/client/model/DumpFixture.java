/*
 * 
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

/**
 * DumpFixture
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2020-12-11T16:57:55.511+03:00[Europe/Moscow]")
public class DumpFixture {
  public static final String SERIALIZED_NAME_APP_NAME = "app_name";
  @SerializedName(SERIALIZED_NAME_APP_NAME)
  private String appName;

  public static final String SERIALIZED_NAME_MODEL_NAME = "model_name";
  @SerializedName(SERIALIZED_NAME_MODEL_NAME)
  private String modelName;

  public static final String SERIALIZED_NAME_FILE_NAME = "file_name";
  @SerializedName(SERIALIZED_NAME_FILE_NAME)
  private String fileName;

  public static final String SERIALIZED_NAME_FILTER_OPTIONS = "filter_options";
  @SerializedName(SERIALIZED_NAME_FILTER_OPTIONS)
  private Object filterOptions;

  public static final String SERIALIZED_NAME_INDENT = "indent";
  @SerializedName(SERIALIZED_NAME_INDENT)
  private Integer indent = 4;


  public DumpFixture appName(String appName) {
    
    this.appName = appName;
    return this;
  }

   /**
   * Get appName
   * @return appName
  **/
  @ApiModelProperty(required = true, value = "")

  public String getAppName() {
    return appName;
  }


  public void setAppName(String appName) {
    this.appName = appName;
  }


  public DumpFixture modelName(String modelName) {
    
    this.modelName = modelName;
    return this;
  }

   /**
   * Get modelName
   * @return modelName
  **/
  @ApiModelProperty(required = true, value = "")

  public String getModelName() {
    return modelName;
  }


  public void setModelName(String modelName) {
    this.modelName = modelName;
  }


  public DumpFixture fileName(String fileName) {
    
    this.fileName = fileName;
    return this;
  }

   /**
   * Get fileName
   * @return fileName
  **/
  @ApiModelProperty(required = true, value = "")

  public String getFileName() {
    return fileName;
  }


  public void setFileName(String fileName) {
    this.fileName = fileName;
  }


  public DumpFixture filterOptions(Object filterOptions) {
    
    this.filterOptions = filterOptions;
    return this;
  }

   /**
   * Get filterOptions
   * @return filterOptions
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getFilterOptions() {
    return filterOptions;
  }


  public void setFilterOptions(Object filterOptions) {
    this.filterOptions = filterOptions;
  }


  public DumpFixture indent(Integer indent) {
    
    this.indent = indent;
    return this;
  }

   /**
   * Get indent
   * @return indent
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Integer getIndent() {
    return indent;
  }


  public void setIndent(Integer indent) {
    this.indent = indent;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DumpFixture dumpFixture = (DumpFixture) o;
    return Objects.equals(this.appName, dumpFixture.appName) &&
        Objects.equals(this.modelName, dumpFixture.modelName) &&
        Objects.equals(this.fileName, dumpFixture.fileName) &&
        Objects.equals(this.filterOptions, dumpFixture.filterOptions) &&
        Objects.equals(this.indent, dumpFixture.indent);
  }

  @Override
  public int hashCode() {
    return Objects.hash(appName, modelName, fileName, filterOptions, indent);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DumpFixture {\n");
    sb.append("    appName: ").append(toIndentedString(appName)).append("\n");
    sb.append("    modelName: ").append(toIndentedString(modelName)).append("\n");
    sb.append("    fileName: ").append(toIndentedString(fileName)).append("\n");
    sb.append("    filterOptions: ").append(toIndentedString(filterOptions)).append("\n");
    sb.append("    indent: ").append(toIndentedString(indent)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}
