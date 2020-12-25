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
 * CheckDocumentFieldFormulaRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2020-12-11T16:57:55.511+03:00[Europe/Moscow]")
public class CheckDocumentFieldFormulaRequest {
  public static final String SERIALIZED_NAME_FORMULA = "formula";
  @SerializedName(SERIALIZED_NAME_FORMULA)
  private String formula;

  public static final String SERIALIZED_NAME_HIDE_UNTIL_PYTHON = "hide_until_python";
  @SerializedName(SERIALIZED_NAME_HIDE_UNTIL_PYTHON)
  private String hideUntilPython;


  public CheckDocumentFieldFormulaRequest formula(String formula) {
    
    this.formula = formula;
    return this;
  }

   /**
   * Get formula
   * @return formula
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getFormula() {
    return formula;
  }


  public void setFormula(String formula) {
    this.formula = formula;
  }


  public CheckDocumentFieldFormulaRequest hideUntilPython(String hideUntilPython) {
    
    this.hideUntilPython = hideUntilPython;
    return this;
  }

   /**
   * Get hideUntilPython
   * @return hideUntilPython
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getHideUntilPython() {
    return hideUntilPython;
  }


  public void setHideUntilPython(String hideUntilPython) {
    this.hideUntilPython = hideUntilPython;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CheckDocumentFieldFormulaRequest checkDocumentFieldFormulaRequest = (CheckDocumentFieldFormulaRequest) o;
    return Objects.equals(this.formula, checkDocumentFieldFormulaRequest.formula) &&
        Objects.equals(this.hideUntilPython, checkDocumentFieldFormulaRequest.hideUntilPython);
  }

  @Override
  public int hashCode() {
    return Objects.hash(formula, hideUntilPython);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CheckDocumentFieldFormulaRequest {\n");
    sb.append("    formula: ").append(toIndentedString(formula)).append("\n");
    sb.append("    hideUntilPython: ").append(toIndentedString(hideUntilPython)).append("\n");
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
