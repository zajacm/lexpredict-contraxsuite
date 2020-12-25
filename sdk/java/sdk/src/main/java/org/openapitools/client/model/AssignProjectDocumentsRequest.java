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
import java.util.ArrayList;
import java.util.List;

/**
 * AssignProjectDocumentsRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2020-12-11T16:57:55.511+03:00[Europe/Moscow]")
public class AssignProjectDocumentsRequest {
  public static final String SERIALIZED_NAME_ASSIGNEE_ID = "assignee_id";
  @SerializedName(SERIALIZED_NAME_ASSIGNEE_ID)
  private Integer assigneeId;

  public static final String SERIALIZED_NAME_ALL = "all";
  @SerializedName(SERIALIZED_NAME_ALL)
  private Boolean all;

  public static final String SERIALIZED_NAME_DOCUMENT_IDS = "document_ids";
  @SerializedName(SERIALIZED_NAME_DOCUMENT_IDS)
  private List<Integer> documentIds = null;

  public static final String SERIALIZED_NAME_NO_DOCUMENT_IDS = "no_document_ids";
  @SerializedName(SERIALIZED_NAME_NO_DOCUMENT_IDS)
  private List<Integer> noDocumentIds = null;


  public AssignProjectDocumentsRequest assigneeId(Integer assigneeId) {
    
    this.assigneeId = assigneeId;
    return this;
  }

   /**
   * Get assigneeId
   * @return assigneeId
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Integer getAssigneeId() {
    return assigneeId;
  }


  public void setAssigneeId(Integer assigneeId) {
    this.assigneeId = assigneeId;
  }


  public AssignProjectDocumentsRequest all(Boolean all) {
    
    this.all = all;
    return this;
  }

   /**
   * Get all
   * @return all
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Boolean getAll() {
    return all;
  }


  public void setAll(Boolean all) {
    this.all = all;
  }


  public AssignProjectDocumentsRequest documentIds(List<Integer> documentIds) {
    
    this.documentIds = documentIds;
    return this;
  }

  public AssignProjectDocumentsRequest addDocumentIdsItem(Integer documentIdsItem) {
    if (this.documentIds == null) {
      this.documentIds = new ArrayList<Integer>();
    }
    this.documentIds.add(documentIdsItem);
    return this;
  }

   /**
   * Get documentIds
   * @return documentIds
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<Integer> getDocumentIds() {
    return documentIds;
  }


  public void setDocumentIds(List<Integer> documentIds) {
    this.documentIds = documentIds;
  }


  public AssignProjectDocumentsRequest noDocumentIds(List<Integer> noDocumentIds) {
    
    this.noDocumentIds = noDocumentIds;
    return this;
  }

  public AssignProjectDocumentsRequest addNoDocumentIdsItem(Integer noDocumentIdsItem) {
    if (this.noDocumentIds == null) {
      this.noDocumentIds = new ArrayList<Integer>();
    }
    this.noDocumentIds.add(noDocumentIdsItem);
    return this;
  }

   /**
   * Get noDocumentIds
   * @return noDocumentIds
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<Integer> getNoDocumentIds() {
    return noDocumentIds;
  }


  public void setNoDocumentIds(List<Integer> noDocumentIds) {
    this.noDocumentIds = noDocumentIds;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AssignProjectDocumentsRequest assignProjectDocumentsRequest = (AssignProjectDocumentsRequest) o;
    return Objects.equals(this.assigneeId, assignProjectDocumentsRequest.assigneeId) &&
        Objects.equals(this.all, assignProjectDocumentsRequest.all) &&
        Objects.equals(this.documentIds, assignProjectDocumentsRequest.documentIds) &&
        Objects.equals(this.noDocumentIds, assignProjectDocumentsRequest.noDocumentIds);
  }

  @Override
  public int hashCode() {
    return Objects.hash(assigneeId, all, documentIds, noDocumentIds);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AssignProjectDocumentsRequest {\n");
    sb.append("    assigneeId: ").append(toIndentedString(assigneeId)).append("\n");
    sb.append("    all: ").append(toIndentedString(all)).append("\n");
    sb.append("    documentIds: ").append(toIndentedString(documentIds)).append("\n");
    sb.append("    noDocumentIds: ").append(toIndentedString(noDocumentIds)).append("\n");
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
