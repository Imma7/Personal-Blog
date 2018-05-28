{% extends 'base.html'%}
{% import "bootstrap/wtf.html" as wtf %}

{% block styles %}
  {{ super() }}
  <link rel="stylesheet" href="{{url_for('static',filename='css/new_posts.css')}}">
{% endblock %}

{% block content%}
<div class="container-fluid">
  <div id="post">
    <div class="col-sm-8">
      {{format_post|safe}}
    </div>
  </div>
</div>


    <div class="container-fluid">
      <div class="title">
        <ul style="list-style-type:none;">
          <li style="font-size:10vh;color:white">{{format_post|safe}}</li>

        </ul>
      </div>
    </div>

    <div class="container-fluid">
      <div class="posts">

        <div class="col-md-4" style="margin-left:5vw;">

          {{ wtf.quick_form(comment_form) }}
          {{simplemde.load}}
        </div>
      </div>
    </div>

      <div id="card" style="margin-top:-20vh; padding-left:10px;">
        <div class="container">
        <p style="font-size:3em;margin-left:-30vw; color:black; font-weight:bolder;">Add Comments</p>
        {% for comment in comment %}
<!-- Card -->
      <div class="card" style="margin-left:31vw;">
        <div class="row">
          <div class="col-md-9">

          <!-- Card content -->
          <div class="card-body">

          <ul>
            <!-- Text -->
            <li class="card-text" style="color:white;font-size:2em">{{comment.comment}}</li>
            <!-- Button -->
          </ul>
        </div>
        </div>
      </div>
    </div>
  </div>
<!-- Card -->
{%endfor%}

</div>

{% endblock %}