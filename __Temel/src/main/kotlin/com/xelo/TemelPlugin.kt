// ! Bu araç @XeloMiso tarafından | @xelo-repo için yazılmıştır.
package com.xelo

import com.lagradost.cloudstream3.plugins.CloudstreamPlugin
import com.lagradost.cloudstream3.plugins.Plugin

@CloudstreamPlugin
class TemelPlugin: Plugin() {
    override fun load() {
        registerMainAPI(Temel())
        registerExtractorAPI(TemelExtractor())
    }
}
