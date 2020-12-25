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
 * SelectProjectsResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2020-12-11T16:57:55.511+03:00[Europe/Moscow]")
public class SelectProjectsResponse {
  public static final String SERIALIZED_NAME_SAVED_FILTER_ID = "saved_filter_id";
  @SerializedName(SERIALIZED_NAME_SAVED_FILTER_ID)
  private Integer savedFilterId;

  public static final String SERIALIZED_NAME_USER_ID = "user_id";
  @SerializedName(SERIALIZED_NAME_USER_ID)
  private Integer userId;

  public static final String SERIALIZED_NAME_PROJECT_IDS = "project_ids";
  @SerializedName(SERIALIZED_NAME_PROJECT_IDS)
  private List<Integer> projectIds = new ArrayList<Integer>();

  public static final String SERIALIZED_NAME_SHOW_WARNING = "show_warning";
  @SerializedName(SERIALIZED_NAME_SHOW_WARNING)
  private Boolean showWarning;


  public SelectProjectsResponse savedFilterId(Integer savedFilterId) {
    
    this.savedFilterId = savedFilterId;
    return this;
  }

   /**
   * Get savedFilterId
   * @return savedFilterId
  **/
  @ApiModelProperty(required = true, value = "")

  public Integer getSavedFilterId() {
    return savedFilterId;
  }


  public void setSavedFilterId(Integer savedFilterId) {
    this.savedFilterId = savedFilterId;
  }


  public SelectProjectsResponse userId(Integer userId) {
    
    this.userId = userId;
    return this;
  }

   /**
   * Get userId
   * @return userId
  **/
  @ApiModelProperty(required = true, value = "")

  public Integer getUserId() {
    return userId;
  }


  public void setUserId(Integer userId) {
    this.userId = userId;
  }


  public SelectProjectsResponse projectIds(List<Integer> projectIds) {
    
    this.projectIds = projectIds;
    return this;
  }

  public SelectProjectsResponse addProjectIdsItem(Integer projectIdsItem) {
    this.projectIds.add(projectIdsItem);
    return this;
  }

   /**
   * Get projectIds
   * @return projectIds
  **/
  @ApiModelProperty(required = true, value = "")

  public List<Integer> getProjectIds() {
    return projectIds;
  }


  public void setProjectIds(List<Integer> projectIds) {
    this.projectIds = projectIds;
  }


  public SelectProjectsResponse showWarning(Boolean showWarning) {
    
    this.showWarning = showWarning;
    return this;
  }

   /**
   * Get showWarning
   * @return showWarning
  **/
  @ApiModelProperty(required = true, value = "")

  public Boolean getShowWarning() {
    return showWarning;
  }


  public void setShowWarning(Boolean showWarning) {
    this.showWarning = showWarning;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SelectProjectsResponse selectProjectsResponse = (SelectProjectsResponse) o;
    return Objects.equals(this.savedFilterId, selectProjectsResponse.savedFilterId) &&
        Objects.equals(this.userId, selectProjectsResponse.userId) &&
        Objects.equals(this.projectIds, selectProjectsResponse.projectIds) &&
        Objects.equals(this.showWarning, selectProjectsResponse.showWarning);
  }

  @Override
  public int hashCode() {
    return Objects.hash(savedFilterId, userId, projectIds, showWarning);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SelectProjectsResponse {\n");
    sb.append("    savedFilterId: ").append(toIndentedString(savedFilterId)).append("\n");
    sb.append("    userId: ").append(toIndentedString(userId)).append("\n");
    sb.append("    projectIds: ").append(toIndentedString(projectIds)).append("\n");
    sb.append("    showWarning: ").append(toIndentedString(showWarning)).append("\n");
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
