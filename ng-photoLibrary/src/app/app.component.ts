import {Component, OnInit} from '@angular/core';
import {AngularFirestore} from '@angular/fire/firestore';
import {Observable} from 'rxjs';
import {PhotoService} from "./photo.service";
import {map} from "rxjs/operators";
import {Photo} from "../models/photo";

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['style/_style.scss']
})
export class AppComponent implements OnInit {
  photos: Observable<Photo[]>;
  currentSessionCount: number = null
  helloMessage: string = ''

  constructor(db: AngularFirestore, private photoService: PhotoService) {
    this.photos = db.collection('currentSession')
      .snapshotChanges()
      .pipe(map(docArray => {
        return docArray.map(doc => {
          return {
            photo_id: doc.payload.doc.id,
            name: doc.payload.doc.data()['name'],
            date: doc.payload.doc.data()['date'],
            thumbnail: doc.payload.doc.data()['thumbnail'],
            path: doc.payload.doc.data()['filepath_raw'],
            jpeg_filepath: doc.payload.doc.data()['filepath_jpeg'],
            thumbnail_filepath: doc.payload.doc.data()['filepath_thumbnail']
          }
        })
      }))
  }

  ngOnInit(): void {
  }

  public onButton() {
    console.log('pushed')
    this.photoService.piCommandHandler('initializeSession')
      .subscribe(data => {
          this.currentSessionCount = data['Message']
          console.log(data)
        }
      )
  }
}
