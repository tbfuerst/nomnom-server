'use strict';
const CACHE_NAME = 'flutter-app-cache';
const RESOURCES = {
  "assets/AssetManifest.json": "148571108d559e2ab2503dc8831496d5",
"assets/FontManifest.json": "01700ba55b08a6141f33e168c4a6c22f",
"assets/fonts/MaterialIcons-Regular.ttf": "56d3ffdef7a25659eab6a68a3fbfaf16",
"assets/LICENSE": "df3260d96acac21a4f8b0d0e07f3bbb4",
"assets/NOTICES": "94e693da13bb641be8259124edd56f8a",
"assets/packages/cupertino_icons/assets/CupertinoIcons.ttf": "115e937bb829a890521f72d2e664b632",
"assets/resources/images/nomnomlogo_book_only.png": "681037028ec5d531cee4b103ec520bd6",
"favicon.png": "9c1d232334a53092f47dc772e92219e7",
"icons/Icon-192.png": "b98f0add57755588536fae5612b1ff57",
"icons/Icon-512.png": "ab1534b25206d7a69e676a73c4a9ca4a",
"index.html": "eabe7e43059289244fd4d708e675f534",
"/": "eabe7e43059289244fd4d708e675f534",
"main.dart.js": "68e33ef395d911651eca85ff96111609",
"manifest.json": "b7ad33cba5328e95cebc3bd988617eb9"
};

self.addEventListener('activate', function (event) {
  event.waitUntil(
    caches.keys().then(function (cacheName) {
      return caches.delete(cacheName);
    }).then(function (_) {
      return caches.open(CACHE_NAME);
    }).then(function (cache) {
      return cache.addAll(Object.keys(RESOURCES));
    })
  );
});

self.addEventListener('fetch', function (event) {
  event.respondWith(
    caches.match(event.request)
      .then(function (response) {
        if (response) {
          return response;
        }
        return fetch(event.request);
      })
  );
});
