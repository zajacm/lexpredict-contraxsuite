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
 * ProjectProgressResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2020-12-11T16:57:55.511+03:00[Europe/Moscow]")
public class ProjectProgressResponse {
  public static final String SERIALIZED_NAME_PROJECT_HAS_COMPLETED_SESSIONS = "project_has_completed_sessions";
  @SerializedName(SERIALIZED_NAME_PROJECT_HAS_COMPLETED_SESSIONS)
  private Boolean projectHasCompletedSessions;

  public static final String SERIALIZED_NAME_USER_UNCOMPLETED_SESSION_PROGRESS = "user_uncompleted_session_progress";
  @SerializedName(SERIALIZED_NAME_USER_UNCOMPLETED_SESSION_PROGRESS)
  private Object userUncompletedSessionProgress;

  public static final String SERIALIZED_NAME_OTHER_UNCOMPLETED_SESSION_PROGRESS = "other_uncompleted_session_progress";
  @SerializedName(SERIALIZED_NAME_OTHER_UNCOMPLETED_SESSION_PROGRESS)
  private Object otherUncompletedSessionProgress;

  public static final String SERIALIZED_NAME_CLUSTERING = "clustering";
  @SerializedName(SERIALIZED_NAME_CLUSTERING)
  private String clustering;

  public static final String SERIALIZED_NAME_REQUIRE_CLUSTERING = "require_clustering";
  @SerializedName(SERIALIZED_NAME_REQUIRE_CLUSTERING)
  private Boolean requireClustering;


  public ProjectProgressResponse projectHasCompletedSessions(Boolean projectHasCompletedSessions) {
    
    this.projectHasCompletedSessions = projectHasCompletedSessions;
    return this;
  }

   /**
   * Get projectHasCompletedSessions
   * @return projectHasCompletedSessions
  **/
  @ApiModelProperty(required = true, value = "")

  public Boolean getProjectHasCompletedSessions() {
    return projectHasCompletedSessions;
  }


  public void setProjectHasCompletedSessions(Boolean projectHasCompletedSessions) {
    this.projectHasCompletedSessions = projectHasCompletedSessions;
  }


  public ProjectProgressResponse userUncompletedSessionProgress(Object userUncompletedSessionProgress) {
    
    this.userUncompletedSessionProgress = userUncompletedSessionProgress;
    return this;
  }

   /**
   * Get userUncompletedSessionProgress
   * @return userUncompletedSessionProgress
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(required = true, value = "")

  public Object getUserUncompletedSessionProgress() {
    return userUncompletedSessionProgress;
  }


  public void setUserUncompletedSessionProgress(Object userUncompletedSessionProgress) {
    this.userUncompletedSessionProgress = userUncompletedSessionProgress;
  }


  public ProjectProgressResponse otherUncompletedSessionProgress(Object otherUncompletedSessionProgress) {
    
    this.otherUncompletedSessionProgress = otherUncompletedSessionProgress;
    return this;
  }

   /**
   * Get otherUncompletedSessionProgress
   * @return otherUncompletedSessionProgress
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(required = true, value = "")

  public Object getOtherUncompletedSessionProgress() {
    return otherUncompletedSessionProgress;
  }


  public void setOtherUncompletedSessionProgress(Object otherUncompletedSessionProgress) {
    this.otherUncompletedSessionProgress = otherUncompletedSessionProgress;
  }


  public ProjectProgressResponse clustering(String clustering) {
    
    this.clustering = clustering;
    return this;
  }

   /**
   * Get clustering
   * @return clustering
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getClustering() {
    return clustering;
  }


  public void setClustering(String clustering) {
    this.clustering = clustering;
  }


  public ProjectProgressResponse requireClustering(Boolean requireClustering) {
    
    this.requireClustering = requireClustering;
    return this;
  }

   /**
   * Get requireClustering
   * @return requireClustering
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Boolean getRequireClustering() {
    return requireClustering;
  }


  public void setRequireClustering(Boolean requireClustering) {
    this.requireClustering = requireClustering;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ProjectProgressResponse projectProgressResponse = (ProjectProgressResponse) o;
    return Objects.equals(this.projectHasCompletedSessions, projectProgressResponse.projectHasCompletedSessions) &&
        Objects.equals(this.userUncompletedSessionProgress, projectProgressResponse.userUncompletedSessionProgress) &&
        Objects.equals(this.otherUncompletedSessionProgress, projectProgressResponse.otherUncompletedSessionProgress) &&
        Objects.equals(this.clustering, projectProgressResponse.clustering) &&
        Objects.equals(this.requireClustering, projectProgressResponse.requireClustering);
  }

  @Override
  public int hashCode() {
    return Objects.hash(projectHasCompletedSessions, userUncompletedSessionProgress, otherUncompletedSessionProgress, clustering, requireClustering);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ProjectProgressResponse {\n");
    sb.append("    projectHasCompletedSessions: ").append(toIndentedString(projectHasCompletedSessions)).append("\n");
    sb.append("    userUncompletedSessionProgress: ").append(toIndentedString(userUncompletedSessionProgress)).append("\n");
    sb.append("    otherUncompletedSessionProgress: ").append(toIndentedString(otherUncompletedSessionProgress)).append("\n");
    sb.append("    clustering: ").append(toIndentedString(clustering)).append("\n");
    sb.append("    requireClustering: ").append(toIndentedString(requireClustering)).append("\n");
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

