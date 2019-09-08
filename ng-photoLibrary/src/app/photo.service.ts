import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {map} from "rxjs/operators";
import {Observable} from "rxjs";
import {Photo} from "../models/photo";
import {AngularFirestore} from "@angular/fire/firestore";

@Injectable({
  providedIn: 'root'
})
export class PhotoService {

  photos: Observable<Photo[]>;

  constructor(private http: HttpClient, private db: AngularFirestore) {
  }

  getLookup() {
    // not configured
  }

  piCommandHandler(commandName, postMethod = 'get', data = {}) {
    let commandUrl = 'http://127.0.0.1:5000/' + commandName
    console.log(commandUrl)
    return this.http[postMethod](commandUrl, data)
  }

  getPhotos() {
    this.photos = this.db.collection('currentSession')
      .snapshotChanges()
      .pipe(map(docArray => {
        return docArray.map(doc => {
          return {
            photo_id: doc.payload.doc.id,
            name: doc.payload.doc.data()['name'],
            date: doc.payload.doc.data()['date'],
            thumbnail_blob: doc.payload.doc.data()['thumbnail_blob'],
            filepath_raw: doc.payload.doc.data()['filepath_raw'],
            filepath_jpeg: doc.payload.doc.data()['filepath_jpeg'],
            filepath_thumbnail: doc.payload.doc.data()['filepath_thumbnail']
          }
        })
      }))
  }
}
