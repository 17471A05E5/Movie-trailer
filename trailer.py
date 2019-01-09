import medias
import fresh_tomatoes

bahubhali2=medias.Tollywoodmovies("bahubhali conclusion",
                  "revenge drama",
                  "https://www.filmibeat.com/ph-big/2015/08/bahubali_143995781800.jpg",
                  "https://youtu.be/G62HrubdD6o")
Srimanthudu=medias.Tollywoodmovies("Srimanthudu conclusion",
                  "simple movie",
                  "https://images.indianexpress.com/2015/08/srimanthudu759.jpg",
                  "https://youtu.be/QSbb2ARJt0s")
_100Love=medias.Tollywoodmovies("100Love conclusion",
                  "heart touching",
                  "https://www.filmibeat.com/ph-big/2011/09/1317277020652961.jpg",
                  "https://youtu.be/yJLDohoU0JE")
Karthikeya=medias.Tollywoodmovies("Karthikeya",
                  "simply superb",
                  "http://www.bharatstudent.com/ng7uvideo/bs/reviews/tel/2735b_Karthikeya-big.jpg",
                  "https://youtu.be/KZy8um0iY9s")
Toliprema=medias.Tollywoodmovies("Toliprema",
                  "awesome movie",
                  "https://www.releasesoon.com/wp-content/uploads/tholi-prema-movie-review.jpg",
                  "https://youtu.be/-kFvrsAgp3M")
movies=[bahubhali2,Srimanthudu,_100Love,Karthikeya,Toliprema]
fresh_tomatoes.open_movies_page(movies)
