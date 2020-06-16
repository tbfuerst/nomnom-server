'use strict';
const CACHE_NAME = 'flutter-app-cache';
const RESOURCES = {
  "main.dart.js": "5ed239fbf2c0d35c5724511fea4d6326",
"index.html": "eabe7e43059289244fd4d708e675f534",
"/": "eabe7e43059289244fd4d708e675f534",
"manifest.json": "b7ad33cba5328e95cebc3bd988617eb9",
"assets/LICENSE": "630b3a020eddecd1a59b9edb71bd2bbb",
"assets/fonts/MaterialIcons-Regular.ttf": "56d3ffdef7a25659eab6a68a3fbfaf16",
"assets/packages/cupertino_icons/assets/CupertinoIcons.ttf": "115e937bb829a890521f72d2e664b632",
"assets/NOTICES": "222f98375866279c6c74a88ce8cb5e26",
"assets/AssetManifest.json": "148571108d559e2ab2503dc8831496d5",
"assets/resources/images/nomnomlogo_book_only.png": "a23fbd30019d5ad3b352f80316ac972d",
"assets/resources/images/examples/exampledish.jpg": "085821f41c7019339276d630d7e35245",
"assets/FontManifest.json": "01700ba55b08a6141f33e168c4a6c22f",
"favicon.png": "9da9ce1c9c1121a48efc2bd9da610e67",
"icons/Icon-192.png": "203b6d6117e6ba2ea9fd658d07135a24",
"icons/Icon-512.png": "25cd80ae8f711af07b19888b68ccebd4"
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
