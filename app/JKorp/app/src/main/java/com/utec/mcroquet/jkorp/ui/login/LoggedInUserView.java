package com.utec.mcroquet.jkorp.ui.login;

import android.content.Intent;
import android.view.View;

import com.utec.mcroquet.jkorp.MainActivity;

/**
 * Class exposing authenticated user details to the UI.
 */
class LoggedInUserView {
    private String displayName;
    //... other data fields that may be accessible to the UI

    LoggedInUserView(String displayName) {
        this.displayName = displayName;
    }

    String getDisplayName() {
        return displayName;
    }

}
