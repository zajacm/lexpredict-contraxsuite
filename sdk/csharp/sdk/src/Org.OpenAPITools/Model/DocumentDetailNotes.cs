/* 
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using OpenAPIDateConverter = Org.OpenAPITools.Client.OpenAPIDateConverter;

namespace Org.OpenAPITools.Model
{
    /// <summary>
    /// DocumentDetailNotes
    /// </summary>
    [DataContract]
    public partial class DocumentDetailNotes :  IEquatable<DocumentDetailNotes>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DocumentDetailNotes" /> class.
        /// </summary>
        [JsonConstructorAttribute]
        protected DocumentDetailNotes() { }
        /// <summary>
        /// Initializes a new instance of the <see cref="DocumentDetailNotes" /> class.
        /// </summary>
        /// <param name="note">note (required).</param>
        /// <param name="timestamp">timestamp.</param>
        /// <param name="user">user.</param>
        /// <param name="locationStart">locationStart.</param>
        /// <param name="locationEnd">locationEnd.</param>
        /// <param name="documentId">documentId (required).</param>
        /// <param name="fieldValueId">fieldValueId.</param>
        /// <param name="fieldId">fieldId.</param>
        public DocumentDetailNotes(string note = default(string), DateTime timestamp = default(DateTime), DocumentDetailUser user = default(DocumentDetailUser), int? locationStart = default(int?), int? locationEnd = default(int?), int documentId = default(int), int fieldValueId = default(int), string fieldId = default(string))
        {
            // to ensure "note" is required (not null)
            if (note == null)
            {
                throw new InvalidDataException("note is a required property for DocumentDetailNotes and cannot be null");
            }
            else
            {
                this.Note = note;
            }
            
            this.LocationStart = locationStart;
            this.LocationEnd = locationEnd;
            // to ensure "documentId" is required (not null)
            if (documentId == null)
            {
                throw new InvalidDataException("documentId is a required property for DocumentDetailNotes and cannot be null");
            }
            else
            {
                this.DocumentId = documentId;
            }
            
            this.Timestamp = timestamp;
            this.User = user;
            this.LocationStart = locationStart;
            this.LocationEnd = locationEnd;
            this.FieldValueId = fieldValueId;
            this.FieldId = fieldId;
        }
        
        /// <summary>
        /// Gets or Sets Pk
        /// </summary>
        [DataMember(Name="pk", EmitDefaultValue=false)]
        public int Pk { get; private set; }

        /// <summary>
        /// Gets or Sets Note
        /// </summary>
        [DataMember(Name="note", EmitDefaultValue=true)]
        public string Note { get; set; }

        /// <summary>
        /// Gets or Sets Timestamp
        /// </summary>
        [DataMember(Name="timestamp", EmitDefaultValue=false)]
        public DateTime Timestamp { get; set; }

        /// <summary>
        /// Gets or Sets User
        /// </summary>
        [DataMember(Name="user", EmitDefaultValue=false)]
        public DocumentDetailUser User { get; set; }

        /// <summary>
        /// Gets or Sets LocationStart
        /// </summary>
        [DataMember(Name="location_start", EmitDefaultValue=true)]
        public int? LocationStart { get; set; }

        /// <summary>
        /// Gets or Sets LocationEnd
        /// </summary>
        [DataMember(Name="location_end", EmitDefaultValue=true)]
        public int? LocationEnd { get; set; }

        /// <summary>
        /// Gets or Sets DocumentId
        /// </summary>
        [DataMember(Name="document_id", EmitDefaultValue=true)]
        public int DocumentId { get; set; }

        /// <summary>
        /// Gets or Sets FieldValueId
        /// </summary>
        [DataMember(Name="field_value_id", EmitDefaultValue=false)]
        public int FieldValueId { get; set; }

        /// <summary>
        /// Gets or Sets FieldId
        /// </summary>
        [DataMember(Name="field_id", EmitDefaultValue=false)]
        public string FieldId { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DocumentDetailNotes {\n");
            sb.Append("  Pk: ").Append(Pk).Append("\n");
            sb.Append("  Note: ").Append(Note).Append("\n");
            sb.Append("  Timestamp: ").Append(Timestamp).Append("\n");
            sb.Append("  User: ").Append(User).Append("\n");
            sb.Append("  LocationStart: ").Append(LocationStart).Append("\n");
            sb.Append("  LocationEnd: ").Append(LocationEnd).Append("\n");
            sb.Append("  DocumentId: ").Append(DocumentId).Append("\n");
            sb.Append("  FieldValueId: ").Append(FieldValueId).Append("\n");
            sb.Append("  FieldId: ").Append(FieldId).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as DocumentDetailNotes);
        }

        /// <summary>
        /// Returns true if DocumentDetailNotes instances are equal
        /// </summary>
        /// <param name="input">Instance of DocumentDetailNotes to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DocumentDetailNotes input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Pk == input.Pk ||
                    (this.Pk != null &&
                    this.Pk.Equals(input.Pk))
                ) && 
                (
                    this.Note == input.Note ||
                    (this.Note != null &&
                    this.Note.Equals(input.Note))
                ) && 
                (
                    this.Timestamp == input.Timestamp ||
                    (this.Timestamp != null &&
                    this.Timestamp.Equals(input.Timestamp))
                ) && 
                (
                    this.User == input.User ||
                    (this.User != null &&
                    this.User.Equals(input.User))
                ) && 
                (
                    this.LocationStart == input.LocationStart ||
                    (this.LocationStart != null &&
                    this.LocationStart.Equals(input.LocationStart))
                ) && 
                (
                    this.LocationEnd == input.LocationEnd ||
                    (this.LocationEnd != null &&
                    this.LocationEnd.Equals(input.LocationEnd))
                ) && 
                (
                    this.DocumentId == input.DocumentId ||
                    (this.DocumentId != null &&
                    this.DocumentId.Equals(input.DocumentId))
                ) && 
                (
                    this.FieldValueId == input.FieldValueId ||
                    (this.FieldValueId != null &&
                    this.FieldValueId.Equals(input.FieldValueId))
                ) && 
                (
                    this.FieldId == input.FieldId ||
                    (this.FieldId != null &&
                    this.FieldId.Equals(input.FieldId))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.Pk != null)
                    hashCode = hashCode * 59 + this.Pk.GetHashCode();
                if (this.Note != null)
                    hashCode = hashCode * 59 + this.Note.GetHashCode();
                if (this.Timestamp != null)
                    hashCode = hashCode * 59 + this.Timestamp.GetHashCode();
                if (this.User != null)
                    hashCode = hashCode * 59 + this.User.GetHashCode();
                if (this.LocationStart != null)
                    hashCode = hashCode * 59 + this.LocationStart.GetHashCode();
                if (this.LocationEnd != null)
                    hashCode = hashCode * 59 + this.LocationEnd.GetHashCode();
                if (this.DocumentId != null)
                    hashCode = hashCode * 59 + this.DocumentId.GetHashCode();
                if (this.FieldValueId != null)
                    hashCode = hashCode * 59 + this.FieldValueId.GetHashCode();
                if (this.FieldId != null)
                    hashCode = hashCode * 59 + this.FieldId.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {

            
            // LocationStart (int?) maximum
            if(this.LocationStart > (int?)2147483647)
            {
                yield return new System.ComponentModel.DataAnnotations.ValidationResult("Invalid value for LocationStart, must be a value less than or equal to 2147483647.", new [] { "LocationStart" });
            }

            // LocationStart (int?) minimum
            if(this.LocationStart < (int?)-2147483648)
            {
                yield return new System.ComponentModel.DataAnnotations.ValidationResult("Invalid value for LocationStart, must be a value greater than or equal to -2147483648.", new [] { "LocationStart" });
            }


            
            // LocationEnd (int?) maximum
            if(this.LocationEnd > (int?)2147483647)
            {
                yield return new System.ComponentModel.DataAnnotations.ValidationResult("Invalid value for LocationEnd, must be a value less than or equal to 2147483647.", new [] { "LocationEnd" });
            }

            // LocationEnd (int?) minimum
            if(this.LocationEnd < (int?)-2147483648)
            {
                yield return new System.ComponentModel.DataAnnotations.ValidationResult("Invalid value for LocationEnd, must be a value greater than or equal to -2147483648.", new [] { "LocationEnd" });
            }

            yield break;
        }
    }

}