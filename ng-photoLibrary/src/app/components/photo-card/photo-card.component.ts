import {Component, Input, OnInit} from '@angular/core';
import {Photo} from "../../../models/photo";

@Component({
  selector: 'app-photo-card',
  templateUrl: './photo-card.component.html',
  styleUrls: ['./photo-card.component.scss']
})
export class PhotoCardComponent implements OnInit {
  @Input()
  photo: Photo

  thumbnail: string

  constructor() {
  }

  ngOnInit() {
    if (this.photo.thumbnail_blob) {
      this.getThumbnail()
    }
  }

  getThumbnail() {
    let photoInBase64 = this.convertToBase64(this.photo.thumbnail_blob)
    this.thumbnail = 'data:image/jpeg;base64,' + photoInBase64
  }

  convertToBase64(blob) {
    return blob.toBase64()
  }

}
