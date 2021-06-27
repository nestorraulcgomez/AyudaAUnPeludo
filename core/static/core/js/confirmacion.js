function confirmarEliminar(id) {
  Swal.fire({
    title: "Estas seguro?",
    text: "No podrás deshacer este cambio!",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Si, Elimínalo!",
    cancelButtonText: "Cancelar",
  }).then((result) => {
    if (result.isConfirmed) {
      window.location.href = "/eliminar_proveedor/" + id;
    }
  });
}
