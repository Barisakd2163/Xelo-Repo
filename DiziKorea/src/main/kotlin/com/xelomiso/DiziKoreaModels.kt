// ! Bu araç @xelomiso tarafından | @XeloRepo için yazılmıştır.

package com.xelomiso

import com.fasterxml.jackson.annotation.JsonProperty

data class KoreaSearch(
    @JsonProperty("theme") val theme: String
)
