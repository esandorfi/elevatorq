const APISRV =
  import.meta.env.DEV && import.meta.env.VITE_APISRV ? import.meta.env.VITE_APISRV : "";

console.log("apisrv used", APISRV);

export default APISRV;
