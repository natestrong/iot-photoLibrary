import {Component, OnInit} from '@angular/core';
import {AngularFirestore} from "@angular/fire/firestore";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'ng-photoLibrary';
  photos = []

  constructor(private db: AngularFirestore) {

  }

  ngOnInit(): void {
    this.db.collection('currentSession')
      .valueChanges()
      .subscribe( result => {
        console.log(result)
        this.photos = result
      })
  }
}


