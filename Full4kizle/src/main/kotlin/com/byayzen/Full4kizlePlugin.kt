// ! Bu araç @XeloMiso tarafından | @xelo-repo için yazılmıştır.
package com.byayzen

import com.lagradost.cloudstream3.plugins.CloudstreamPlugin
import com.lagradost.cloudstream3.plugins.Plugin

@CloudstreamPlugin
class Full4kizlePlugin: Plugin() {
    override fun load() {
        registerMainAPI(Full4kizle())
        registerExtractorAPI(HotstreamExtractor())
    }
}
