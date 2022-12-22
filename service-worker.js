navigator.serviceWorker.register('/service-worker.js').then(function(registration) {
    // Registro exitoso
    console.log('ServiceWorker registrado exitosamente con scope: ', registration.scope);
  }, function(err) {
    // Registro fallido
    console.log('ServiceWorker falló al registrarse: ', err);
  });
  