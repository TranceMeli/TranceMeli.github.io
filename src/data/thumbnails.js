// Kleine Vorschaubilder (WebP) in src/assets/thumbs/, benannt nach "<projekt-id>-<nr>.webp".
// Fehlt zu einem Screenshot die Vorschau, wird stattdessen das Originalbild geladen.
const files = import.meta.glob('../assets/thumbs/*.webp', {
  eager: true,
  query: '?url',
  import: 'default',
})

export function thumbnailFor(projectId, index) {
  return files[`../assets/thumbs/${projectId}-${index}.webp`] ?? null
}
