// ! Bu araç @xelomiso tarafından | @XeloRepo için yazılmıştır.

package com.xelomiso

import com.fasterxml.jackson.annotation.JsonProperty


data class AjaxSource(
    @JsonProperty("status")      val status: String,
    @JsonProperty("iframe")      val iframe: String,
    @JsonProperty("alternative") val alternative: String,
)
