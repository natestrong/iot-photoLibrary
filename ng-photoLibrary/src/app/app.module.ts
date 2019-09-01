import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {BrowserAnimationsModule} from "@angular/platform-browser/animations";
import {MaterialModule} from "./material.module";
import {AngularFireModule} from "@angular/fire";
import {environment} from "../environments/environment";
import {AngularFirestoreModule} from "@angular/fire/firestore";

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MaterialModule,
    AngularFireModule.initializeApp(
      environment.firebase
    ),
    AngularFirestoreModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
