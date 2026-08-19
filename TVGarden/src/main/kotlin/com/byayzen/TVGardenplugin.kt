// ! Bu araç @ByAyzen tarafından | @cs-xelo için yazılmıştır.
package com.byayzen

import com.lagradost.cloudstream3.plugins.CloudstreamPlugin
import com.lagradost.cloudstream3.plugins.BasePlugin

@CloudstreamPlugin
class TVGardenplugin: BasePlugin() {
    override fun load() {
        registerMainAPI(TVGarden())
    }
}

