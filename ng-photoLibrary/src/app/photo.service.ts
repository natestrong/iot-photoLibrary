import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class PhotoService {

  constructor(private http: HttpClient) {
  }

  getLookup() {
    // not configured
  }

  piCommandHandler(commandName, postMethod = 'get', data = {}) {
    let commandUrl = 'http://127.0.0.1:5000/' + commandName
    console.log(commandUrl)
    return this.http[postMethod](commandUrl)
  }
}
