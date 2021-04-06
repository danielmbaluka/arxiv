import {NgModule} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import {ArticlesComponent} from './articles/articles.component';
import {AuthorsComponent} from './authors/authors.component';
import {ArticleDetailsComponent} from './articles/details/article-details.component';
import {AuthorDetailsComponent} from './authors/author-details/author-details.component';
import {RegisterComponent} from './auth/register/register.component';


const routes: Routes = [
  {
    path: '',
    redirectTo: '/articles',
    pathMatch: 'full'
  },
  {
    path: 'register',
    component: RegisterComponent
  },
  {
    path: 'articles',
    component: ArticlesComponent
  },
  {
    path: 'articles/:id',
    component: ArticleDetailsComponent
  },
  {
    path: 'authors',
    component: AuthorsComponent
  },
  {
    path: 'authors/:id',
    component: AuthorDetailsComponent
  },
  {
    path: '**',
    redirectTo: '/articles'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
