const search = document.querySelector('#search');
const buttons = [...document.querySelectorAll('[data-filter]')];
const cards = [...document.querySelectorAll('.card')];
let category = '全部';
function filter() {
  const words = search.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
  let visible = 0;
  for (const card of cards) {
    const text = (card.textContent + ' ' + card.dataset.search).toLowerCase();
    card.hidden = (category !== '全部' && category !== card.dataset.kind) || !words.every(word => text.includes(word));
    if (!card.hidden) visible++;
  }
  document.querySelector('#count').textContent = visible + ' 个插件';
  document.querySelector('#empty').hidden = visible !== 0;
}
search.addEventListener('input',filter);
for (const button of buttons) button.addEventListener('click',() => {
  category = button.dataset.filter;
  for (const item of buttons) item.setAttribute('aria-pressed', String(item === button));
  filter();
});
