// ! Bu araç @ByAyzen tarafından | @Xeloanime için yazılmıştır.
package com.byayzen

import com.lagradost.cloudstream3.plugins.CloudstreamPlugin
import com.lagradost.cloudstream3.plugins.Plugin

@CloudstreamPlugin
class SubspleasePlugin: Plugin() {
    override fun load() {
        registerMainAPI(Subsplease())
    }
}
