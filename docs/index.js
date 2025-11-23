$(() => {
    const params = new URLSearchParams(window.location.search);
    console.log('params', params)
    const id = params.has('p') ? params.get('p') : 'P001';
    console.log('id', id)
    $('#image').load(`data/tree-${id}.dot.svg`, () => {
        $('#image a').on('click', function (e) {
            const nextId = $(e.target).closest('a').attr('xlink:href').substring(1)
            console.log('nextId', nextId);

            const url = new URL(window.location.href);
            const base = `${url.origin}${url.pathname}?p=${nextId}`;
            console.log('base', base);

            window.location.href=base;
        })
    })
});
