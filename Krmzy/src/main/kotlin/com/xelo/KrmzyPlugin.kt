// ! Bu araç @XeloMiso tarafından | @Xeloanime için yazılmıştır.
package com.xelo

import com.lagradost.cloudstream3.plugins.CloudstreamPlugin
import com.lagradost.cloudstream3.plugins.Plugin

@CloudstreamPlugin
class KrmzyPlugin: Plugin() {
    override fun load() {
        registerMainAPI(Krmzy())
        registerExtractorAPI(TurkveArabExtractor())
        registerExtractorAPI(ArabveTurk())
        registerExtractorAPI(iPlayerHls())
    }
}
