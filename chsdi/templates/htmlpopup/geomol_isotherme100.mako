<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geomol-isotherme_100.elev')}</td>    	<td>${c['attributes']['elev'] or '-'}</td></tr>
</%def>

