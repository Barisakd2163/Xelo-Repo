// ! Bu araç @XeloMiso tarafından | @Xeloanime için yazılmıştır.
package com.xelo

import com.lagradost.cloudstream3.extractors.PixelDrain
import com.lagradost.cloudstream3.plugins.CloudstreamPlugin
import com.lagradost.cloudstream3.plugins.Plugin

@CloudstreamPlugin
class AnimeAVPlugin: Plugin() {
    override fun load() {
        registerMainAPI(AnimeAV())
        registerExtractorAPI(Mp4Upload())
        registerExtractorAPI(PixelDrain())
        registerExtractorAPI(AnimeAVHLS())
        registerExtractorAPI(AnimeavUPNS())
    }
}
