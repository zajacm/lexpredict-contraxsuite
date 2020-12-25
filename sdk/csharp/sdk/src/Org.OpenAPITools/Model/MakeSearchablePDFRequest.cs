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
    /// MakeSearchablePDFRequest
    /// </summary>
    [DataContract]
    public partial class MakeSearchablePDFRequest :  IEquatable<MakeSearchablePDFRequest>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="MakeSearchablePDFRequest" /> class.
        /// </summary>
        /// <param name="documentIds">documentIds.</param>
        public MakeSearchablePDFRequest(List<int> documentIds = default(List<int>))
        {
            this.DocumentIds = documentIds;
        }
        
        /// <summary>
        /// Gets or Sets DocumentIds
        /// </summary>
        [DataMember(Name="document_ids", EmitDefaultValue=false)]
        public List<int> DocumentIds { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class MakeSearchablePDFRequest {\n");
            sb.Append("  DocumentIds: ").Append(DocumentIds).Append("\n");
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
            return this.Equals(input as MakeSearchablePDFRequest);
        }

        /// <summary>
        /// Returns true if MakeSearchablePDFRequest instances are equal
        /// </summary>
        /// <param name="input">Instance of MakeSearchablePDFRequest to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(MakeSearchablePDFRequest input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.DocumentIds == input.DocumentIds ||
                    this.DocumentIds != null &&
                    input.DocumentIds != null &&
                    this.DocumentIds.SequenceEqual(input.DocumentIds)
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
                if (this.DocumentIds != null)
                    hashCode = hashCode * 59 + this.DocumentIds.GetHashCode();
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
            yield break;
        }
    }

}