import { Component } from '@angular/core';

@Component({
    selector: 'my-app',
    templateUrl: 'static/NgApp/partials/test.html'
})

export class AppComponent {
    name: string;
    artists: string[];

    constructor() {
        this.name = 'Bib';
        this.artists = [
            {
                name: 'one'
            },
            {
                name: 'two'
            }
            ];
    }
}
