// ! Bu araç @XeloMiso tarafından | @Xeloanime için yazılmıştır.
package com.xelo

import com.lagradost.cloudstream3.plugins.CloudstreamPlugin
import com.lagradost.cloudstream3.plugins.Plugin

@CloudstreamPlugin
class EsheaqPlugin: Plugin() {
    override fun load() {
        registerMainAPI(Esheaq())
        registerExtractorAPI(VidSpeedExtractor())
        registerExtractorAPI(VidSpeedCC())
        registerExtractorAPI(VDeskExtractor())
        registerExtractorAPI(VidObaExtractor())
        registerExtractorAPI(VidObaCCExtractor())
        registerExtractorAPI(VAlbrqExtractor())
        registerExtractorAPI(VidSpeed())
    }
}
