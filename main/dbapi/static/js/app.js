//jQuery global code

$(document).ready(function (){

	// Toggles the sidebar
	$("#sidenav-toggle").click(function (){
		if ($("#sidebar-wrapper").hasClass("closed")){
			$("#sidenav-toggle").removeClass("fa-bars");
			$("#sidenav-toggle").addClass("fa-minus");
			$("#sidebar-wrapper").removeClass("closed");
			$("#sidebar-wrapper").addClass("opened");
		}
		else{
			$("#sidenav-toggle").removeClass("fa-minus");
			$("#sidenav-toggle").addClass("fa-bars");
			$("#sidebar-wrapper").removeClass("opened");
			$("#sidebar-wrapper").addClass("closed");
		}
	});

	$("#footer-toggle").click(function () {
		if ($("#footer-wrapper").hasClass("footer-closed")){
			$("#footer-wrapper").removeClass("footer-closed");
			$("#footer-wrapper").addClass("footer-opened");
		}
		else{
			$("#footer-wrapper").removeClass("footer-opened");
			$("#footer-wrapper").addClass("footer-closed");
		}
	});
});

//Angular get calls



var main = angular.module('main', ['ngRoute', 'ngCookies']);

main.config(function($routeProvider){
	$routeProvider

		.when('/', {
			templateUrl : '../static/html/home.html',
			controller : 'mainCtrl'
		})

		.when('/photography', {
			templateUrl : '../static/html/photography.html',
			controller : 'collectionsCtrl'
		})

		.when('/photography/:name*', {
			templateUrl : '../static/html/gallery.html',
			controller : 'galleryCtrl'
		})

		.when('/blog', {
			templateUrl: '../static/html/blog.html',
			controller : 'blogCtrl'
		})

		.when('/teams', {
			templateUrl: '../static/html/teams.html',
			controller : 'teamsCtrl'
		})

		.when('/projects', {
			templateUrl: '../static/html/projects.html',
			controller : 'projectsCtrl'
		})

		.when('/projects/:name*', {
			templateUrl: '../static/html/projectlist.html',
			controller : 'projectlistCtrl'
		})

		.when('/about', {
			templateUrl: '../static/html/about.html',
			controller : 'aboutCtrl'
		});

});

main.controller('mainCtrl', function($scope, $http, $sce){
	$http.get("/api/posts/")
	.then(function(response){
		response.data.results[0].body = $sce.trustAsHtml(response.data.results[0].body)
		$scope.latest = response.data.results[0]
		$http.get("/api/posts/"+String($scope.latest.pk)+"/photos/")
		.then(function(response){
			if (response.data != '') {
				for (i=0; i < response.data.length; i++) {
					response.data[i].image = '..'.concat(response.data[i].image.substring(10));
				}
				$scope.photo = response.data[0].image;
			}
			else {
				$scope.photo = ""
			}
		});
	});
});

var arr = {};
main.controller('blogCtrl', function($scope, $http, $compile, getPostPhotos){
	var x;
	$http.get("/api/posts/")
	.then(function(response){
		for (i = 0; i < response.data.count; i++) {
		 	(function(x){
				getPostPhotos.req(x, function(callback){
					arr[String(x)] = callback;
				});	
			})(response.data.results[i].pk);
		}
		$scope.posts = response.data.results;
		$scope.photos = arr;
	});
});

main.controller('teamsCtrl', function($scope, $http, getTeamPhotos){
	var x;
	$http.get("/api/teams/")
	.then(function(response){
		for (i = 0; i < response.data.count; i++) {
		 	(function(x){
				getTeamPhotos.req(x, function(callback){
					arr[String(x)] = callback;
				});	
			})(response.data.results[i].pk);
		}
		$scope.teams = response.data.results;
		$scope.photos = arr;
	});
	$scope.increment = function(teampk, curr){
		if (curr < arr[teampk].length - 1) {
			return curr + 1
		}
		else {
			return 0
		}
	}
	$scope.range = function(teampk){

		var ratings = []; 

		for (var i = 0; i < arr[teampk].length; i++) { 
			ratings.push(i) 
		} 

		return ratings;
	}
	$scope.cnt = function(teampk){
		return arr[teampk].length - 1;
	}
});

main.controller('projectsCtrl', function($scope, $http, pkStore){
	$http.get("/api/categories/")
	.then(function(response){
		$scope.categories = response.data.results;
	});
	$scope.npk = function(pk){
		pkStore.updatecategorypk(pk);
	}
});

main.controller('projectlistCtrl', function($scope, $http, getProjectPhotos, pkStore){
	var x;
	var catpk = pkStore.categorypk();
	$http.get("/api/categories/" + String(catpk) + "/projects/")
	.then(function(response){
		for (i = 0; i < response.data.length; i++) {
		 	(function(x){
				getProjectPhotos.req(catpk, x, function(callback){
					arr[String(x)] = callback;
				});	
			})(response.data[i].pk);
		}
		$scope.projects = response.data;
		$scope.photos = arr;
	});
	$scope.increment = function(projpk, curr){
		if (curr < arr[projpk].length - 1) {
			return curr + 1
		}
		else {
			return 0
		}
	}
	$scope.range = function(projpk){

		var ratings = []; 

		for (var i = 0; i < arr[projpk].length; i++) { 
			ratings.push(i) 
		} 

		return ratings;
	}
	$scope.cnt = function(projpk){
		return arr[projpk].length - 1;
	}
});


main.controller('aboutCtrl', function($scope){
	$scope.message = "Section in development";
});

main.controller('collectionsCtrl', function($scope, $http, pkStore){
	$http.get("/api/collections/")
	.then(function(response){
		$scope.content = response.data.results.chunk(2);
	});
	$scope.npk = function(pk){
		pkStore.updategallerypk(pk);
	}
	$scope.getPhoto = function(item, pk) {
		$http.get("/api/collections/"+String(pk)+"/photos/")
		.then(function(response){
			if (response.data != '') {
				for (i=0; i < response.data.length; i++) {
					response.data[i].image = '..'.concat(response.data[i].image.substring(10));
				}
				item.photo = response.data[0].image;
			}
			else {
				item.photo = "";
			}
		});
	}
});

main.factory( 'pkStore', function($cookies) {
	return {
		gallerypk: function() {return $cookies.get('gallery');},
		updategallerypk: function(npk){
			$cookies.put('gallery', npk);
				return $cookies.get('gallery');
		},
		categorypk: function() {return $cookies.get('category');},
		updatecategorypk: function(npk){
			$cookies.put('category', npk);
				return $cookies.get('category')
		}
	}
});

main.factory('getPostPhotos', function($http) {
    return {
        req: function(pk, callback) {
        	$http.get("/api/posts/" + String(pk) + "/photos/")
			.then(function(response){
			for (j=0; j < response.data.length; j++) {
				response.data[j].image = '..'.concat(response.data[j].image.substring(10));
			}
			callback(response.data)
			});
		}
    };
});


main.factory('getTeamPhotos', function($http) {
    return {
        req: function(pk, callback) {
        	$http.get("/api/teams/" + String(pk) + "/photos/")
			.then(function(response){
			for (j=0; j < response.data.length; j++) {
				response.data[j].image = '..'.concat(response.data[j].image.substring(10));
			}
			callback(response.data)
			});
		}
    };
});

main.factory('getProjectPhotos', function($http) {
    return {
        req: function(catpk, projpk, callback) {
        	$http.get("/api/categories/" + String(catpk) + "/projects/" + String(projpk) + "/photos/")
			.then(function(response){
			for (j=0; j < response.data.length; j++) {
				response.data[j].image = '..'.concat(response.data[j].image.substring(10));
			}
			callback(response.data)
			});
		}
    };
});

main.controller('galleryCtrl', function($scope, $http, $timeout, pkStore){
	$http.get("/api/collections/" + pkStore.gallerypk() + "/photos/")
	.then(function(response){
		if (response.data != '') {
			for (i=0; i < response.data.length; i++) {
				response.data[i].image = '..'.concat(response.data[i].image.substring(10));
			}
		}
		$scope.content = response.data;
	});
	$scope.index = 0;
	$scope.setindex = function(inp){
		$scope.startFade = true;
		$timeout(function(){
			$scope.hide = true;
            
            $scope.startFade=false;
        }, 240);
        $timeout(function(){
        	$scope.index=inp;
        }, 250);
        $timeout(function(){
            $scope.startFadein=true;
        }, 270);
        $timeout(function(){
			$scope.hide = false;
            $scope.startFadein=false;
        }, 518);
	}
	$scope.increment = function(){
		$scope.startFade = true;
		$timeout(function(){
			$scope.hide = true;
            
            $scope.startFade=false;
        }, 240);
        $timeout(function(){
        	$scope.index += 1;
        }, 250);
        $timeout(function(){
            $scope.startFadein=true;
        }, 270);
        $timeout(function(){
			$scope.hide = false;
            $scope.startFadein=false;
        }, 518);
  	};
  	$scope.decrement = function(){
  		$scope.startFade = true;
		$timeout(function(){
			$scope.hide = true;
            
            $scope.startFade=false;
        }, 240);
        $timeout(function(){
        	$scope.index -= 1;
        }, 250);
        $timeout(function(){
            $scope.startFadein=true;
        }, 270);
        $timeout(function(){
			$scope.hide = false;
            $scope.startFadein=false;
        }, 518);
  	};
});




Array.prototype.chunk = function(chunkSize) {
    var array=this;
    return [].concat.apply([],
        array.map(function(elem,i) {
            return i%chunkSize ? [] : [array.slice(i,i+chunkSize)];
        })
    );
}

main.directive('dynamic', function ($compile) {
  return {
    restrict: 'A',
    replace: true,
    link: function (scope, ele, attrs) {
      scope.$watch(attrs.dynamic, function(html) {
        ele.html(html);
        $compile(ele.contents())(scope);
      });
    }
  };
});