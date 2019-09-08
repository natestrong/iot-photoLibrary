import {Component, Input, OnInit} from '@angular/core';
import {Photo} from "../../../models/photo";
import {DomSanitizer} from "@angular/platform-browser";

@Component({
  selector: 'app-photo-card',
  templateUrl: './photo-card.component.html',
  styleUrls: ['./photo-card.component.scss']
})
export class PhotoCardComponent implements OnInit {
  @Input()
  photo: Photo

  thumbnail: any

  constructor(private sanitizer: DomSanitizer) {
  }

  ngOnInit() {
    if (this.thumbnail) {
      this.getThumbnail()
    }
  }

  getThumbnail() {
    let photoInBase64 = this.convertToBase64(this.photo.thumbnail)
    this.thumbnail = this.sanitizer.bypassSecurityTrustResourceUrl('data:image/jpeg;base64,' + photoInBase64)
  }

  convertToBase64(blob) {
    return blob.toBase64()
  }

}
