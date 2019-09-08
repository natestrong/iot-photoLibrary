import {Component, OnInit} from '@angular/core';
import {PhotoService} from "../../photo.service";

@Component({
  selector: 'app-photo-card-list',
  templateUrl: './photo-card-list.component.html',
  styleUrls: ['./photo-card-list.component.scss']
})
export class PhotoCardListComponent implements OnInit {

  constructor(public photoService: PhotoService) {
  }

  ngOnInit() {
    this.photoService.getPhotos()
  }

}
