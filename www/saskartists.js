SaskArtists = {
  get: function(argument, def) {
    return (new URL(window.location.href)).searchParams.get(argument) || def;
  },
  getLink: function(target, argument, def) {
    return target.replace("$", SaskArtists.get(argument, def));
  }
}
