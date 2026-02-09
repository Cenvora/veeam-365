from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTSshSettingsFromClient")


@_attrs_define
class RESTSshSettingsFromClient:
    """Specifies credentials to access the Linux-based backup proxy server.

    Attributes:
        account (str | Unset): Specifies a name of the SSH user account.
        account_password (str | Unset): Specifies a password.
        port (int | None | Unset): Specifies a port number which is used to connect to the specified backup proxy server
            through SSH. The default value is *22*.
        connection_timeout (int | None | Unset): Specifies the SSH connection timeout in *milliseconds*. This timeout is
            used to wait for connection to the specified backup proxy server through SSH. The default value is *30000*.
        private_key_base_64 (None | str | Unset): Specifies the content of the private key file provided as a Base64
            string.
        private_key_passphrase (str | Unset): Specifies a password.
        elevate_account_to_root (bool | None | Unset): Defines whether the SSH user account privileges will be elevated
            in case of insufficient privileges.
        add_to_sudoers (bool | None | Unset): Defines whether the SSH user account will be added to the *Sudoers* group.
        use_su_if_sudo_unavailable (bool | None | Unset): Defines whether it is allowed to use `SU` if `sudo` is
            unavailable.
        root_password (str | Unset): Specifies a password.
        fingerprint (None | str | Unset): Specifies the SSH fingerprint.
        public_base_64_key (None | str | Unset): Specifies the content of the public key file provided as a Base64
            string.

            **Note**: This property is required to verify connection.
        ignore_fingerprint_check (bool | None | Unset): Defines whether to skip verification of the SSH fingerprint.
    """

    account: str | Unset = UNSET
    account_password: str | Unset = UNSET
    port: int | None | Unset = UNSET
    connection_timeout: int | None | Unset = UNSET
    private_key_base_64: None | str | Unset = UNSET
    private_key_passphrase: str | Unset = UNSET
    elevate_account_to_root: bool | None | Unset = UNSET
    add_to_sudoers: bool | None | Unset = UNSET
    use_su_if_sudo_unavailable: bool | None | Unset = UNSET
    root_password: str | Unset = UNSET
    fingerprint: None | str | Unset = UNSET
    public_base_64_key: None | str | Unset = UNSET
    ignore_fingerprint_check: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account = self.account

        account_password = self.account_password

        port: int | None | Unset
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        connection_timeout: int | None | Unset
        if isinstance(self.connection_timeout, Unset):
            connection_timeout = UNSET
        else:
            connection_timeout = self.connection_timeout

        private_key_base_64: None | str | Unset
        if isinstance(self.private_key_base_64, Unset):
            private_key_base_64 = UNSET
        else:
            private_key_base_64 = self.private_key_base_64

        private_key_passphrase = self.private_key_passphrase

        elevate_account_to_root: bool | None | Unset
        if isinstance(self.elevate_account_to_root, Unset):
            elevate_account_to_root = UNSET
        else:
            elevate_account_to_root = self.elevate_account_to_root

        add_to_sudoers: bool | None | Unset
        if isinstance(self.add_to_sudoers, Unset):
            add_to_sudoers = UNSET
        else:
            add_to_sudoers = self.add_to_sudoers

        use_su_if_sudo_unavailable: bool | None | Unset
        if isinstance(self.use_su_if_sudo_unavailable, Unset):
            use_su_if_sudo_unavailable = UNSET
        else:
            use_su_if_sudo_unavailable = self.use_su_if_sudo_unavailable

        root_password = self.root_password

        fingerprint: None | str | Unset
        if isinstance(self.fingerprint, Unset):
            fingerprint = UNSET
        else:
            fingerprint = self.fingerprint

        public_base_64_key: None | str | Unset
        if isinstance(self.public_base_64_key, Unset):
            public_base_64_key = UNSET
        else:
            public_base_64_key = self.public_base_64_key

        ignore_fingerprint_check: bool | None | Unset
        if isinstance(self.ignore_fingerprint_check, Unset):
            ignore_fingerprint_check = UNSET
        else:
            ignore_fingerprint_check = self.ignore_fingerprint_check

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account is not UNSET:
            field_dict["account"] = account
        if account_password is not UNSET:
            field_dict["accountPassword"] = account_password
        if port is not UNSET:
            field_dict["port"] = port
        if connection_timeout is not UNSET:
            field_dict["connectionTimeout"] = connection_timeout
        if private_key_base_64 is not UNSET:
            field_dict["privateKeyBase64"] = private_key_base_64
        if private_key_passphrase is not UNSET:
            field_dict["privateKeyPassphrase"] = private_key_passphrase
        if elevate_account_to_root is not UNSET:
            field_dict["elevateAccountToRoot"] = elevate_account_to_root
        if add_to_sudoers is not UNSET:
            field_dict["addToSudoers"] = add_to_sudoers
        if use_su_if_sudo_unavailable is not UNSET:
            field_dict["UseSuIfSudoUnavailable"] = use_su_if_sudo_unavailable
        if root_password is not UNSET:
            field_dict["rootPassword"] = root_password
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if public_base_64_key is not UNSET:
            field_dict["publicBase64Key"] = public_base_64_key
        if ignore_fingerprint_check is not UNSET:
            field_dict["ignoreFingerprintCheck"] = ignore_fingerprint_check

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account = d.pop("account", UNSET)

        account_password = d.pop("accountPassword", UNSET)

        def _parse_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        port = _parse_port(d.pop("port", UNSET))

        def _parse_connection_timeout(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        connection_timeout = _parse_connection_timeout(d.pop("connectionTimeout", UNSET))

        def _parse_private_key_base_64(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        private_key_base_64 = _parse_private_key_base_64(d.pop("privateKeyBase64", UNSET))

        private_key_passphrase = d.pop("privateKeyPassphrase", UNSET)

        def _parse_elevate_account_to_root(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        elevate_account_to_root = _parse_elevate_account_to_root(d.pop("elevateAccountToRoot", UNSET))

        def _parse_add_to_sudoers(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        add_to_sudoers = _parse_add_to_sudoers(d.pop("addToSudoers", UNSET))

        def _parse_use_su_if_sudo_unavailable(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_su_if_sudo_unavailable = _parse_use_su_if_sudo_unavailable(d.pop("UseSuIfSudoUnavailable", UNSET))

        root_password = d.pop("rootPassword", UNSET)

        def _parse_fingerprint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fingerprint = _parse_fingerprint(d.pop("fingerprint", UNSET))

        def _parse_public_base_64_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_base_64_key = _parse_public_base_64_key(d.pop("publicBase64Key", UNSET))

        def _parse_ignore_fingerprint_check(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        ignore_fingerprint_check = _parse_ignore_fingerprint_check(d.pop("ignoreFingerprintCheck", UNSET))

        rest_ssh_settings_from_client = cls(
            account=account,
            account_password=account_password,
            port=port,
            connection_timeout=connection_timeout,
            private_key_base_64=private_key_base_64,
            private_key_passphrase=private_key_passphrase,
            elevate_account_to_root=elevate_account_to_root,
            add_to_sudoers=add_to_sudoers,
            use_su_if_sudo_unavailable=use_su_if_sudo_unavailable,
            root_password=root_password,
            fingerprint=fingerprint,
            public_base_64_key=public_base_64_key,
            ignore_fingerprint_check=ignore_fingerprint_check,
        )

        rest_ssh_settings_from_client.additional_properties = d
        return rest_ssh_settings_from_client

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
