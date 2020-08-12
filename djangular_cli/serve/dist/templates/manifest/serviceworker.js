// Base Service Worker implementation.  To use your own Service Worker, set the SERVICE_WORKER_PATH variable in settings.py

var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
    '/offline/',
    '/assets/ng_css/styles.css',
     '/assets/ng_js/runtime.js',
     '/assets/ng_js/polyfills.js',
     '/assets/ng_js/scripts.js',
     '/assets/ng_js/webphotofilter.js',
     '/assets/ng_js/webphotofilter/webphotofilter.ts3tvfuf.js',
     '/assets/ng_js/webphotofilter/hgl7dero.entry.js',
     '/assets/ng_js/main.js',
    '/assets/img/icon-72x72.png',
    '/assets/img/icon-96x96.png',
    '/assets/img/icon-128x128.png',
    '/assets/img/icon-144x144.png',
    '/assets/img/icon-152x152.png',
    '/assets/img/icon-192x192.png',
    '/assets/img/icon-384x384.png',
    '/assets/img/icon-512x512.png',
    '/assets/img/splash-640x1136.png',
    '/assets/img/splash-750x1334.png',
    '/assets/img/splash-1242x2208.png',
    '/assets/img/splash-1125x2436.png',
    '/assets/img/splash-828x1792.png',
    '/assets/img/splash-1242x2688.png',
    '/assets/img/splash-1536x2048.png',
    '/assets/img/splash-1668x2224.png',
    '/assets/img/splash-1668x2388.png',
    '/assets/img/splash-2048x2732.png'
];

// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
            .catch(() => {
                return caches.match('/offline/');
            })
    )
});
