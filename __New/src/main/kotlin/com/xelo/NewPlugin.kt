// ! This Extension Made By @XeloMiso for GizliKeyif

package com.xelo

import com.lagradost.cloudstream3.plugins.CloudstreamPlugin
import com.lagradost.cloudstream3.plugins.Plugin
import android.content.Context

@CloudstreamPlugin
class NewPlugin: Plugin() {
    override fun load() {
        registerMainAPI(New())
    }
}
