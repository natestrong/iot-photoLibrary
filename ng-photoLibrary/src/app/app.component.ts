import {Component, OnInit} from '@angular/core';
import {PhotoService} from "./photo.service";
import {MatProgressButtonOptions} from "mat-progress-buttons";

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['style/_style.scss']
})
export class AppComponent implements OnInit {
  helloMessage: string = ''

  refreshButtonOptions: MatProgressButtonOptions = {
    active: false,
    text: 'Refresh',
    spinnerSize: 18,
    raised: true,
    fab: true,
    stroked: false,
    buttonColor: 'primary',
    spinnerColor: 'accent',
    fullWidth: false,
    disabled: false,
    mode: 'indeterminate',
    icon: 'refresh'
  }

  hardRefreshButtonOptions: MatProgressButtonOptions = {
    active: false,
    text: 'Hard Refresh',
    buttonColor: 'accent',
    barColor: 'primary',
    raised: true,
    stroked: false,
    mode: 'indeterminate',
    value: 0,
    disabled: false,
    fullWidth: false
  }


  constructor(private photoService: PhotoService) {
  }

  ngOnInit(): void {
    this.onRefresh(false)
    this.hardRefreshButtonOptions.active = true;
  }

  public onRefresh(deleteFirst) {
    console.log('Refreshing')

    if (deleteFirst) {
      this.hardRefreshButtonOptions.active = true;
    } else {
      this.refreshButtonOptions.active = true;
    }

    this.photoService.piCommandHandler(
      'initializeSession',
      'post',
      {'deleteFirst': deleteFirst})
      .subscribe(data => {
          this.helloMessage = data['Message']
          console.log(data)
          this.refreshButtonOptions.active = false;
          this.hardRefreshButtonOptions.active = false;
        }
      )
  }
}
